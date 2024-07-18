from db.connection import create_connection
from mysql.connector import Error

def execute_query(query, params=None, fetch_one=False):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor(dictionary=True)
        try:
            cursor.execute(query, params)
            connection.commit()
            if fetch_one:
                return cursor.fetchone()
            return cursor.fetchall()
        except Error as e:
            return f"Errore durante l'esecuzione della query: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"

def add_payment_method(email, metodo_pagamento):
    query = "INSERT INTO METODO_PAGAMENTO (email, metodo) VALUES (%s, %s)"
    params = (email, metodo_pagamento)
    return execute_query(query, params)

def place_order(email, annunci):
    query = "INSERT INTO ORDINE (email, id_annuncio) VALUES (%s, %s)"
    for annuncio in annunci:
        params = (email, annuncio)
        result = execute_query(query, params)
        if "Errore" in result:
            return result
    return "Ordine eseguito con successo"

def get_order_history(email):
    query = """
    SELECT o.idOrdine, o.email, o.codStato, a.titolo, a.descrizione, a.prezzo
    FROM ORDINE o
    JOIN DETTAGLIO_ORDINE do ON o.idOrdine = do.idOrdine
    JOIN ANNUNCIO a ON do.id_annuncio = a.id_annuncio
    WHERE o.email = %s
    """
    params = (email,)
    return execute_query(query, params)

def get_subscription_options():
    query = "SELECT tipoAbbonamento, durata, prezzo FROM ABBONAMENTO"
    return execute_query(query)

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

def get_best_sellers():
    query = """
    SELECT v.email, AVG(r.valutazione) as media_valutazione
    FROM VENDITORE v
    JOIN RECENSIONE r ON v.email = r.email_venditore
    GROUP BY v.email
    ORDER BY media_valutazione DESC
    LIMIT 5
    """
    return execute_query(query)

def get_worst_sellers():
    query = """
    SELECT v.email, AVG(r.valutazione) as media_valutazione
    FROM VENDITORE v
    JOIN RECENSIONE r ON v.email = r.email_venditore
    GROUP BY v.email
    ORDER BY media_valutazione ASC
    LIMIT 5
    """
    return execute_query(query)

def get_buyable_announcment():
    query = """
    SELECT id_annuncio
    FROM ANNUNCIO a
    LEFT JOIN DETTAGLIO_ORDINE do ON a.id_annuncio = do.id_annuncio
    WHERE do.id_annuncio IS NULL
    """
    result = execute_query(query)
    list_annunci = [r['id_annuncio'] for r in result]
    return list_annunci