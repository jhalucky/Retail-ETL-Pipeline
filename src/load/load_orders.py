from src.config.database import get_connection


def load_orders(df):
    """ Load orders data from a DataFrame into the orders table in the PostgreSQL database."""

    connection = get_connection()
    cursor = connection.cursor()
    
    for row in df.itertuples(index=False):

        cursor.execute(
            """ INSERT INTO orders (order_id, customer_id, order_date, payment_method, order_status)
                VALUES (%s, %s, %s, %s, %s)"""

                (
                    row.order_id,
                    row.customer_id,
                    row.order_date,
                    row.payment_method,
                    row.order_status
                )
        )


    connection.commit()
    cursor.close()
    connection.close()

    print("Orders data loaded successfully into the database.")