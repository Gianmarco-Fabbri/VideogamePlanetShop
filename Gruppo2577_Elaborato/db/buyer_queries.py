from db.connection import create_connection
from mysql.connector import Error

def execute_query(query, params=None, fetch=False):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            if fetch:
                result = cursor.fetchall()
                return result
            else:
                connection.commit()
                return "Esecuzione terminata con successo"
        except Error as e:
            connection.rollback()
            return f"Errore durante l'esecuzione della query: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"

def add_payment_method(email, tipologia, circuito, codice, scadenza):
    query = """
    INSERT INTO METODO_PAGAMENTO (tipologiaCarta, circuitoPagamento, codCarta, scadenza, email)
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (tipologia, circuito, codice, scadenza, email)
    return execute_query(query, params)

def generaID():
    query = """
    SELECT idOrdine 
    FROM ORDINE
    ORDER BY idOrdine DESC
    LIMIT 1
    """
    result = execute_query(query, fetch=True)

    if result and len(result) > 0:
        return result[0]['idOrdine'] + 1
    else:
        return 1  # Se non ci sono 0 ordini, inizia da 1

def place_order(email, id_annunci):
    idOrdine = generaID()

    query_ordine = "INSERT INTO ORDINE (idOrdine, email, codStato) VALUES (%s, %s, %s)"
    params_ordine = (idOrdine, email, '0')
    result_ordine = execute_query(query_ordine, params_ordine)
    if "Errore" in result_ordine:
        return result_ordine

    query_get_email = "SELECT email FROM ANNUNCIO WHERE id_annuncio = %s"
    query_dettOrdine = "INSERT INTO DETTAGLIO_ORDINE (id_annuncio, email, idOrdine) VALUES (%s, %s, %s)"
    query_tracciamento = '''
    INSERT INTO TRACCIAMENTO (città, cap, via, numero, id_annuncio, nome_magazzino)
    VALUES (%s, %s, %s, %s, %s, %s)
    '''

    for annuncio in id_annunci:
        # Recupera l'email del venditore per ogni annuncio
        params_get_email = (annuncio,)
        result_get_email = execute_query(query_get_email, params_get_email, fetch=True)
        if not result_get_email:
            return f"Errore: Annuncio con ID {annuncio} non trovato."
        
        venditore_email = result_get_email[0]['email']

        params_dett = (annuncio, venditore_email, idOrdine)
        result_dett = execute_query(query_dettOrdine, params_dett)
        if "Errore" in result_dett:
            return result_dett

        params_tracc = ("Bologna", 40126, "Via Rizzoli", 1, annuncio, "Magazzino Start")
        result_tracc = execute_query(query_tracciamento, params_tracc)
        if "Errore" in result_tracc:
            return result_tracc

    return "Ordine eseguito con successo"

def get_order_history(email):
    query = """
    SELECT *
    FROM ORDINE o
    WHERE o.email = %s
    """
    params = (email,)
    return execute_query(query, params, fetch=True)

def get_subscription_options():
    query = "SELECT tipoAbbonamento, durata, prezzo FROM ABBONAMENTO"
    result = execute_query(query, fetch=True)

    if result and isinstance(result, list):
        options = [opt['tipoAbbonamento'] for opt in result if 'tipoAbbonamento' in opt]
    else:
        options = []

    return options

def subscribe(email, tipoAbbonamento):
    query = '''INSERT INTO STORICO (email, tipoAbbonamento, data_inizio, data_fine) 
    VALUES (%s, %s, CURDATE(), DATE_ADD(CURDATE(), 
    INTERVAL (SELECT durata FROM ABBONAMENTO WHERE tipoAbbonamento = %s) DAY))
    '''
    params = (email, tipoAbbonamento, tipoAbbonamento)
    return execute_query(query, params)

def leave_review(email_compratore, email_venditore, recensione, punteggio):
    query = "INSERT INTO RECENSIONE (email_acquirente, email_venditore, descrizione, valutazione) VALUES (%s, %s, %s, %s)"
    params = (email_compratore, email_venditore, recensione, punteggio)
    return execute_query(query, params)

def top3_products():
    query="""
    SELECT prodotto.descrizione, COUNT(*)
    FROM ANNUNCIO JOIN DETTAGLIO ON
    (annuncio.id_annuncio = dettaglio.id_annuncio) join specifiche_prodotto on 
    (specifiche_prodotto.codice = dettaglio.codice AND specifiche_prodotto.numeroSerie = dettaglio.numeroSerie) join prodotto on
    (specifiche_prodotto.codice = prodotto.codice)
    group by prodotto.codice DESC
    Limit 3"""
    return execute_query(query)

def get_subscription_history(email):
    query = """
    SELECT tipoAbbonamento, data_inizio, data_fine
    FROM STORICO
    WHERE email = %s
    ORDER BY data_inizio DESC
    """
    params = (email,)
    return execute_query(query, params, fetch=True)


def get_best_sellers():
    query = """
    SELECT v.email, AVG(r.valutazione) as media_valutazione
    FROM VENDITORE v
    JOIN RECENSIONE r ON v.email = r.email_venditore
    GROUP BY v.email
    ORDER BY media_valutazione DESC
    LIMIT 3
    """
    result = execute_query(query, fetch=True)
    return result

def get_worst_sellers():
    query = """
    SELECT v.email, AVG(r.valutazione) as media_valutazione
    FROM VENDITORE v
    JOIN RECENSIONE r ON v.email = r.email_venditore
    GROUP BY v.email
    ORDER BY media_valutazione ASC
    LIMIT 3
    """
    result = execute_query(query, fetch=True)
    return result

def get_buyable_announcment():
    query = """
    SELECT a.id_annuncio, a.titolo, a.email, a.descrizione
    FROM ANNUNCIO a
    LEFT JOIN DETTAGLIO_ORDINE do ON a.id_annuncio = do.id_annuncio
    WHERE do.id_annuncio IS NULL
    """
    result = execute_query(query, fetch=True)
    list_annunci = [{'id': r['id_annuncio'], 'titolo': r['titolo'], 'email': r['email'], 'descrizione': r['descrizione']} for r in result]
    return list_annunci