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
    
def generaID():
    query = """
    SELECT id_annuncio 
    FROM ANNUNCIO 
    ORDER BY id_annuncio DESC
    LIMIT 1
    """
    result = execute_query(query, fetch=True)

    if result and len(result) > 0:
        return result[0]['id_annuncio'] + 1
    else:
        return 1  # Se non ci sono annunci, inizia da 1

def check_block(email):
    query_check_block = """
    SELECT isBloccato FROM VENDITORE WHERE email = %s
    """
    params_check_block = (email,)
    result_check_block = execute_query(query_check_block, params_check_block, fetch=True)
    
    return result_check_block

def create_annuncio(email, titolo, descrizione, prezzo, 
                    codice, numeroDiSerie, descrizioneProdotto, colore="-",
                    isUsato=0, condizioni="-"):
    
    blocked = check_block(email)
    if not blocked or blocked[0]['isBloccato'] == 1:
        return "Non è possibile creare un annuncio, il venditore è bloccato."
    
    punti_prodotto = int(int(prezzo) * 10)
    id_annuncio = generaID()

    query1 = """
    INSERT INTO SPECIFICHE_PRODOTTO (codice, descrizione, numeroSerie, colore)
    VALUES (%s, %s, %s, %s)
    """
    params1 = (codice, descrizioneProdotto, numeroDiSerie, colore)

    query2 = """
    INSERT INTO ANNUNCIO (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email, sconto)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    params2 = (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email, 0)

    query3 = """
    INSERT INTO DETTAGLIO (isUsato, condizioni, id_annuncio, email, codice, numeroSerie)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params3 = (isUsato, condizioni, id_annuncio, email, codice, numeroDiSerie)

    result1 = execute_query(query1, params1)
    if result1 is None:
        return "Inserimento interrotto, non esiste alcun prodotto con il codice specificato"

    result2 = execute_query(query2, params2)
    if "Errore" in result2:
        return "Vendita annuncio bloccata"

    result3 = execute_query(query3, params3)
    if "Errore" in result3:
        return "Esecuzione inserimento dettaglio non avvenuta"

    return "Annuncio creato con successo"

def modify_annuncio(email, id_annuncio,
                    codice, numeroDiSerie, descrizioneProdotto, colore="-",
                    isUsato=0, condizioni="-"):
    
    blocked = check_block(email)
    if not blocked or blocked[0]['isBloccato'] == 1:
        return "Non è possibile modificare alcun annuncio, il venditore è bloccato."
    
    query_check = "SELECT * FROM ANNUNCIO WHERE id_annuncio = %s AND email = %s"
    params_check = (id_annuncio, email)
    result_check = execute_query(query_check, params_check, fetch=True)
    
    if not result_check:
        return "Annuncio non trovato"
    
    query_specifica = """
    INSERT INTO SPECIFICHE_PRODOTTO (codice, descrizione, numeroSerie, colore)
    VALUES (%s, %s, %s, %s)
    """
    params_specifica = (codice, descrizioneProdotto, numeroDiSerie, colore)
    
    result_specifica = execute_query(query_specifica, params_specifica)
    if isinstance(result_specifica, str) and "Errore" in result_specifica:
        return result_specifica
    
    # Inserisci il dettaglio del prodotto
    query_dettaglio = """
    INSERT INTO DETTAGLIO (isUsato, condizioni, id_annuncio, email, codice, numeroSerie)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    params_dettaglio = (isUsato, condizioni, id_annuncio, email, codice, numeroDiSerie)
    
    result_dettaglio = execute_query(query_dettaglio, params_dettaglio)
    if isinstance(result_dettaglio, str) and "Errore" in result_dettaglio:
        return result_dettaglio
    
    return "Specifiche del prodotto aggiunte all'annuncio."

def delete_annuncio(email, id_annuncio):
    query1 = "DELETE FROM DETTAGLIO WHERE id_annuncio = %s AND email = %s"
    query2 = "DELETE FROM ANNUNCIO WHERE id_annuncio = %s AND email = %s"
    params = (id_annuncio, email)

    connection = create_connection() 
    if connection is not None:
        cursor = connection.cursor()
        try:
            cursor.execute(query1, params)
            cursor.execute(query2, params)
            connection.commit()
            return "Annuncio eliminato con successo"
        except Error as e:
            connection.rollback()
            print(f"Errore durante l'eliminazione dell'annuncio: {e}")
            return f"Errore durante l'eliminazione dell'annuncio: {e}"
        finally:
            cursor.close()
            connection.close()
    else:
        return "Connessione al database fallita"

def apply_discount(email, id_annuncio, sconto):

    query = '''UPDATE ANNUNCIO 
    SET sconto = %s, prezzo = prezzo * (1 - %s / 100) 
    WHERE email = %s AND id_annuncio = %s
    '''
    params = (sconto, sconto, email, id_annuncio)
    return execute_query(query, params)

def my_annunci(email):
    query = "SELECT * FROM ANNUNCIO WHERE email = %s"
    params = (email,)
    return execute_query(query, params, fetch=True)

def my_recensioni(email):
    query = "SELECT * FROM RECENSIONE WHERE email_venditore = %s"
    params = (email,)
    
    return execute_query(query, params, fetch=True)