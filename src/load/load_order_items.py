from src.config.database import get_connection

def load_order_items(df):

    """ Loads order items data from a DF into order_items table in the PostgreSQL database."""
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        for row in df.itertuples(index=False):
            cursor.execute(
                """ INSERT INTO order_items(order_item_id, order_id, product_id, quantity, unit_price)
                    VALUES (%s, %s, %s, %s, %s)
                """,
                (
                    row.order_item_id,
                    row.order_id,
                    row.product_id,
                    row.quantity,
                    row.unit_price
                )
            )

        connection.commit()


    except Exception as e:
        print(f"Error loading order items data: {e}")
        if connection:
            connection.rollback()

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    