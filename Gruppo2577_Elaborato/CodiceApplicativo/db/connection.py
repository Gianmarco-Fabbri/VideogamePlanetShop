import mysql.connector
from mysql.connector import Error, connect
from config import DB_CONFIG

def create_connection():
    try:
        connection = connect(
            host=DB_CONFIG['host'],
            database=DB_CONFIG['database'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password']
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Errore durante la connessione al database: {e}")
        return None