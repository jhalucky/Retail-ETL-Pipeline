from src.config.database import get_connection

def load_products(df):
    """Loads the products DataFrame into the PostgreSQL database."""
    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        for row in df.itertuples(index=False):

            cursor.execute(
                """ 
                INSERT INTO products (product_id, product_name, category, brand, price, stock_quantity)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (row.product_id, row.product_name, row.category, row.brand, row.price, row.stock_quantity)
            )



        connection.commit()

    except Exception as e:
        print(f"Error loading products data: {e}")
        if connection:
            connection.rollback()
            
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


    print("Product data loaded successfully into the database.")