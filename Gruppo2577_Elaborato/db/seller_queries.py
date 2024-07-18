from db.connection import create_connection
from mysql.connector import Error

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
    
def generaID():
    query = """
    SELECT id_annuncio 
    FROM ANNUNCIO 
    ORDER BY id_annuncio DESC
    LIMIT 1
    """
    result = execute_query(query, fetch_one=True)

    if result:
        return result['id_annuncio'] + 1
    else:
        return 1  # Se non ci sono annunci, inizia da 1

def create_annuncio(email, titolo, descrizione, prezzo, 
                    codice, numeroDiSerie, descrizioneProdotto, colore="-",
                    isUsato=0, codizioni="-"):
    
    punti_prodotto = int(prezzo * 10)
    id_annuncio = generaID()

    query = """
    INSERT INTO ANNUNCIO (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email)
    VALUES (%s, %s, %s, %s, %s)
    """

    query2="""
    INSERT INTO SPECIFICHE_PRODOTTO (codice, descrizione, numeroSerie, colore)
    VALUES (%s, %s, %s, %s)"""

    query3="""
    INSERT INTO DETTAGLIO (isUsato,condizioni,id_annuncio,codice,numeroSerie)
    VALUES (%s, %s, %s, %s, %s)
    """
    params = (punti_prodotto, id_annuncio, titolo, prezzo, descrizione, email)
    params2=(codice,descrizioneProdotto,numeroDiSerie,colore)
    params3=(isUsato,codizioni,id_annuncio,codice,numeroDiSerie)

    flag = execute_query(query, params)
    if flag=="Esecuzione terminata con successo":
        flag2=execute_query(query2, params2)
        if flag2=="Esecuzione terminata con successo":
            return execute_query(query3,params3)
        else:
            return "Esecuzione inserimento dettaglio non avvenuta"
    else:
        return "Esecuzione inserimento specifica prodotto non avvenuta"
        
        
'''create view prodotti_scontati AS
select annuncio.id_annuncio,
annuncio.prezzo * (sconto.percentuale/100) as prezzo_scontato
from annuncio join sconto on (annuncio.id_annuncio = sconto.id_annuncio)'''


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