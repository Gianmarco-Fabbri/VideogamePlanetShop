from db.connection import create_connection
from mysql.connector import Error

def add_user(email, nome, nome_account, password, ruolo, città, cap, via, numero):
    ruolo_column = {
        "compratore": "ACQUIRENTE",
        "venditore": "VENDITORE"
    }
    query = """
    INSERT INTO UTENTE (nome, email, nome_account, password, ACQUIRENTE, ADMIN, VENDITORE, città, cap, via, numero) 
    VALUES (%s, %s, %s, %s, %s, NULL, %s, %s, %s, %s, %s)
    """
    params = (nome, email, nome_account, password, 
              email if ruolo == "compratore" else None, email if ruolo == "venditore" else None, 
              città, cap, via, numero)
    return execute_query(query, params)

def block_user(email):
    if not is_seller(email):
        return "L'email specificata non appartiene ad alcun venditore"

    query = "UPDATE UTENTE SET VENDITORE = NULL WHERE email = %s"
    params = (email,)
    return execute_query(query, params)

def unblock_user(email):
    if not is_seller(email):
        return "L'email specificata non appartiene ad alcun venditore"
    
    query = "UPDATE UTENTE SET VENDITORE = %s WHERE email = %s"
    params = (email, email)
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
            connection.commit()
            return "Esecuzione terminata con successo"
        except Error as e:
            return f"Errore durante l'esecuzione: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"
    
def is_seller(email):
    query = "SELECT email FROM VENDITORE WHERE email = %s"
    params = (email,)
    connection = create_connection()
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            return result is not None
        except Error as e:
            return False
        finally:
            cursor.close()
            connection.close()
    else:
        return False