from src.config.database import get_connection

def load_payments(df):
    """ Loads payments data from a DF into payments table in the PostgreSQL database."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        for row in df.itertuples(index=False):
            cursor.execute(
                """ INSERT INTO payments(payment_id, order_id, payment_method,payment_status, payment_date)
                    VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    row.payment_id,
                    row.order_id,
                    row.payment_method,
                    row.payment_status,
                    row.payment_date
                )
            )

        connection.commit()

    except Exception as e:
        print(f"Error loading payments data: {e}")
        if connection:
            connection.rollback()
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    print("Payments data loaded successfully into the database.")