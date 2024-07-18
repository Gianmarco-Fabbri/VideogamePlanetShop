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

def subscribe(email):
    query = "UPDATE COMPRATORE SET isAbbonato = 1 WHERE email = %s"
    params = (email,)
    return execute_query(query, params)

def leave_review(email_compratore, email_venditore, recensione, punteggio):
    query = "INSERT INTO RECENSIONE (email_compratore, email_venditore, recensione, punteggio) VALUES (%s, %s, %s, %s)"
    params = (email_compratore, email_venditore, recensione, punteggio)
    return execute_query(query, params)

def get_best_sellers():
    query = """
    SELECT v.email, AVG(r.punteggio) as media_punteggio
    FROM VENDITORE v
    JOIN RECENSIONE r ON v.email = r.email_venditore
    GROUP BY v.email
    ORDER BY media_punteggio DESC
    LIMIT 5
    """
    return execute_query(query)

def get_worst_sellers():
    query = """
    SELECT v.email, AVG(r.punteggio) as media_punteggio
    FROM VENDITORE v
    JOIN RECENSIONE r ON v.email = r.email_venditore
    GROUP BY v.email
    ORDER BY media_punteggio ASC
    LIMIT 5
    """
    return execute_query(query)