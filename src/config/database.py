import psycopg2

from dotenv import load_dotenv
import os   

load_dotenv()

def get_connection():
    """ Establishes a connection to the PostgreSQL database and returns the connection object. """

    connection = psycopg2.connect (
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "retail_db"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "luckysince2005"),
        port=os.getenv("DB_PORT", "5432")
    )


    return connection