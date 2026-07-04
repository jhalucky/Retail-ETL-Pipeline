from src.config.database import get_connection
from src.config.logger import logger

def load_customers(df):

    """ Loads customer data from a DataFrame into the customers table in the PostgreSQL database."""


    connection = get_connection()
    cursor = connection.cursor()

    for row in df.itertuples(index=False):
        cursor.execute(
            """
               INSERT INTO customers (
                    customer_id,
                    first_name,
                    last_name,
                    gender,
                    email,
                    phone,
                    address,
                    city,
                    state,
                    signup_date
               )

               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                row.customer_id,
                row.first_name,
                row.last_name,
                row.gender,
                row.email,
                row.phone,
                row.address,
                row.city,
                row.state,
                row.signup_date

            )
        )


    connection.commit()

    cursor.close()
    connection.close()
    logger.info("Customer data loaded successfully into the database.")

    # print("Customer data loaded successfully into the database.")