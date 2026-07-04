from src.config.database import get_connection


def load_orders(df):
    """ Load orders data from a DataFrame into the orders table in the PostgreSQL database."""
     
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        for row in df.itertuples(index=False):

            cursor.execute(
                """ INSERT INTO orders (order_id, customer_id, order_date, order_status, total_amount)
                    VALUES (%s, %s, %s, %s, %s)""",

                    (
                        row.order_id,
                        row.customer_id,
                        row.order_date,
                        row.order_status,
                        row.total_amount
                    )
            )


        connection.commit()

    except Exception as e:
        print(f"Error loading orders data: {e}")
        if connection:
            connection.rollback()
    
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    print("Orders data loaded successfully into the database.")