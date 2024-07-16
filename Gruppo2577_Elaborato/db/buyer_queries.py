from db.connection import create_connection
from mysql.connector import Error

def execute_buyer_query(query, params=None):
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

def get_buyer_purchases(buyer_email):
    query = "SELECT * FROM Acquisti WHERE acquirente_email = %s"
    params = (buyer_email,)
    return execute_buyer_query(query, params)