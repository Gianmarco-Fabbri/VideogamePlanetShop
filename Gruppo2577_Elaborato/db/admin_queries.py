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
    
    query2 = "INSERT INTO VENDITORE (email, isBloccato, isNegozio) VALUES (%s, %s, %s)"
    query3 = "INSERT INTO ACQUIRENTE (isAbbonato, email, puntiSconto) VALUES (%s, %s, %s)"
    params2 = (email, 0, 0)
    params3 = (0, email, 0)

    flag = execute_query(query, params)

    if flag == "Esecuzione terminata con successo":
        return execute_query(query3, params3) if ruolo == "compratore" else execute_query(query2, params2)
    return flag

def block_user(email):
    if not is_seller(email):
        return "L'email specificata non appartiene ad alcun venditore"
    
    if isSellerBlocked(email):
        return "L'utente specificato è già bloccato"

    query = "UPDATE VENDITORE SET isBloccato = 1 WHERE email = %s"
    params = (email,)
    return execute_query(query, params)

def unblock_user(email):
    if not is_seller(email):
        return "L'email specificata non appartiene ad alcun venditore"
    
    if not isSellerBlocked(email):
        return "L'utente specificato non è bloccato"
    
    query = "UPDATE VENDITORE SET isBloccato = 0 WHERE email = %s"
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
    
def isSellerBlocked(email):
    query = "SELECT isBloccato FROM VENDITORE WHERE email = %s"
    params = (email,)
    connection = create_connection()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute(query, params)
            result = cursor.fetchone()
            if result:
                return result[0] == 1
            else:
                print("Utente non trovato.")
                return False
        except Error as e:
            print(f"Errore nell'esecuzione: {e}")
            return False
        finally:
            cursor.close()
            connection.close()
    else:
        print("Connessione al database fallita.")
        return False