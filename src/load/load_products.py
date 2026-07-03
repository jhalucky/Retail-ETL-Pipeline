from src.config.database import get_connection

def load_products(df):
    """Loads the products DataFrame into the PostgreSQL database."""

    connection = get_connection()
    cursor = connection.cursor()

    for row in df.itertuples(index=False):
        print(
    f"product_id={row.product_id}, "
    f"product_name={row.product_name}, "
    f"category={row.category}, "
    f"brand={row.brand}, "
    f"price={row.price}, "
    f"stock_quantity={row.stock_quantity}"
)
        cursor.execute(
            """ 
            INSERT INTO products (product_id, product_name, category, brand, price, stock_quantity)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (row.product_id, row.product_name, row.category, row.brand, row.price, row.stock_quantity)
        )



    connection.commit()
    cursor.close()
    connection.close()


    print("Product data loaded successfully into the database.")