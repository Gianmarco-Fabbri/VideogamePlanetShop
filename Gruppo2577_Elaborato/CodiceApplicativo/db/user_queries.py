from db.connection import create_connection
from mysql.connector import Error

def get_user_type(email, password):
    connection = create_connection() 
    if connection is not None:
        cursor = connection.cursor()
        try:
            # Verifica le credenziali dell'utente
            user_query = "SELECT * FROM utente WHERE email = %s AND password = %s"
            cursor.execute(user_query, (email, password))
            user = cursor.fetchone()
            if not user:
                return None  # Utente non trovato o credenziali non valide

            # Verifica se l'utente è un amministratore
            admin_query = "SELECT email FROM ADMIN WHERE email = %s"
            cursor.execute(admin_query, (email,))
            admin = cursor.fetchone()
            if admin:
                return "admin"

            # Verifica se l'utente è un venditore
            seller_query = "SELECT email FROM VENDITORE WHERE email = %s"
            cursor.execute(seller_query, (email,))
            seller = cursor.fetchone()
            if seller:
                return "seller"

            # Verifica se l'utente è un acquirente
            buyer_query = "SELECT email FROM ACQUIRENTE WHERE email = %s"
            cursor.execute(buyer_query, (email,))
            buyer = cursor.fetchone()
            if buyer:
                return "buyer"

            return None
        except Error as e:
            return f"Errore durante l'esecuzione della query: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"