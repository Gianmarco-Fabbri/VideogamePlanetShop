from db.connection import create_connection
from mysql.connector import Error

def create_annuncio(email, titolo, descrizione, prezzo):
    punti_prodotto = int(prezzo * 10)
    id_annuncio = 1000

    query = """
    INSERT INTO ANNUNCIO (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email)
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email)
    return execute_query(query, params)

def delete_annuncio(email, id_annuncio):
    query = "DELETE FROM ANNUNCIO WHERE email = %s AND id_annuncio = %s"
    params = (email, id_annuncio)
    return execute_query(query, params)

def apply_discount(email, id_annuncio, sconto):
    #query per predere il prezzo dell'annuncio e calcolare lo sconto --> scontoreale = 
    query = "UPDATE ANNUNCIO SET prezzo = prezzo - %s WHERE email = %s AND id_annuncio = %s"
    params = (sconto, email, id_annuncio)
    return execute_query(query, params)

def product_best_seller():
    query = """
    SELECT p.descrizione, p.codice, p.CONSOLE, p.ACCESSORIO, p.GIOCO, p.idCasaProduttrice, p.numeroGenerazione, COUNT(*) as num_vendite
    FROM PRODOTTO p
    JOIN ANNUNCIO a ON p.codice = a.id_annuncio
    GROUP BY p.descrizione, p.codice, p.CONSOLE, p.ACCESSORIO, p.GIOCO, p.idCasaProduttrice, p.numeroGenerazione
    ORDER BY num_vendite DESC
    LIMIT 1
    """
    return execute_query(query, fetch_one=True)

def my_annunci(email):
    query = "SELECT * FROM ANNUNCIO WHERE email = %s"
    params = (email,)
    return execute_query(query, params)

def execute_query(query, params=None):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            return f"Errore durante l'esecuzione della query: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"