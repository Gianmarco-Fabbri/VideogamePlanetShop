from db.connection import create_connection
from mysql.connector import Error

def execute_admin_query(query):
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query)
            connection.commit()
            return "Query eseguita con successo"
        except Error as e:
            return f"Errore durante l'esecuzione della query: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"

def get_all_products():
    return execute_admin_query('SELECT * FROM Prodotti as p WHERE p.Colore = "nero"')

# Altre query per amministratori possono essere aggiunte qui