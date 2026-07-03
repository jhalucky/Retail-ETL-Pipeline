import psycopg2

def get_connection():
    """ Establishes a connection to the PostgreSQL database and returns the connection object. """

    connection = psycopg2.connect (
        host="localhost",
        database="retail_db",
        user="postgres",
        password="luckysince2005",
        port='5432'
    )

    return connection