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

def has_payment_method(email):
    query = "SELECT COUNT(*) as count FROM METODO_PAGAMENTO WHERE email = %s"
    params = (email,)
    result = execute_query(query, params, fetch=True)
    
    if result and result[0]['count'] > 0:
        return True
    else:
        return False

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

    if not has_payment_method(email):
        return "Errore: Nessun metodo di pagamento registrato. Aggiungi un metodo di pagamento prima di effettuare un ordine."
    
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
    if not has_payment_method(email):
        return "Nessun metodo di pagamento registrato. Aggiungi un metodo di pagamento prima di abbonarti."

    query_check_abbonamento = """
    SELECT COUNT(*) as abbonamento_attivo
    FROM STORICO
    WHERE email = %s AND data_fine >= CURDATE()
    """
    params_check_abbonamento = (email,)
    result_check_abbonamento = execute_query(query_check_abbonamento, params_check_abbonamento, fetch=True)

    if result_check_abbonamento and result_check_abbonamento[0]['abbonamento_attivo'] > 0:
        return "Errore: Hai già un abbonamento attivo"

    query_storico = '''INSERT INTO STORICO (email, tipoAbbonamento, data_inizio, data_fine) 
    VALUES (%s, %s, CURDATE(), DATE_ADD(CURDATE(), 
    INTERVAL (SELECT durata FROM ABBONAMENTO WHERE tipoAbbonamento = %s) DAY))
    '''
    params_storico = (email, tipoAbbonamento, tipoAbbonamento)

    result_storico = execute_query(query_storico, params_storico)
    if "Errore" in result_storico:
        return result_storico

    query_acquirente = "UPDATE ACQUIRENTE SET isAbbonato = 1 WHERE email = %s"
    params_acquirente = (email,)

    result_acquirente = execute_query(query_acquirente, params_acquirente)
    if "Errore" in result_acquirente:
        return result_acquirente

    return "Abbonamento effettuato con successo"

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

def tracking(email):
    query_abbonato = """
    SELECT *
    FROM ACQUIRENTE
    WHERE email = %s AND isAbbonato = 1
    """
    params_abbonato = (email,)
    result_abbonato = execute_query(query_abbonato, params_abbonato, fetch=True)

    if result_abbonato and result_abbonato[0]['isAbbonato'] == 0:
        return "Tracciamento non disponibile: l'utente non è abbonato"

    query = """
    SELECT tr.id_annuncio, do.idOrdine, tr.nome_magazzino, so.descrizione as stato
    FROM TRACCIAMENTO tr
    JOIN DETTAGLIO_ORDINE do ON tr.id_annuncio = do.id_annuncio
    JOIN ORDINE o ON do.idOrdine = o.idOrdine
    JOIN STATO_ORDINE so ON o.codStato = so.codStato
    WHERE o.email = %s
    """
    params = (email,)
    return execute_query(query, params, fetch=True)

def get_valutazioni_medie_venditori():
    query = """
    SELECT email_venditore, AVG(valutazione) as valutazione_media
    FROM RECENSIONE
    GROUP BY email_venditore
    ORDER BY valutazione_media ASC
    LIMIT 5
    """
    return execute_query(query, fetch=True)

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