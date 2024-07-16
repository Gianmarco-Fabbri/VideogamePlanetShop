from db.connection import create_connection
from mysql.connector import Error

def execute_seller_query(query, params=None):
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

def get_seller_products(seller_email):
    query = "SELECT * FROM Prodotti WHERE venditore_email = %s"
    params = (seller_email,)
    return execute_seller_query(query, params)