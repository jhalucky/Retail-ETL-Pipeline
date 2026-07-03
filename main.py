from src.extract.read_csv import read_csv
from src.validate.duplicates import validate_duplicate_rows, validate_duplicate_primary_keys
from src.validate.emails import validate_emails
from src.validate.missing import validate_missing_values
from src.validate.phone import validate_phone_numbers
from src.validate.schema import validate_schema
from src.tranform.trim_whitespace  import trim_whitespace


customers_df =  read_csv('data/raw/customers.csv')
orders_df = read_csv('data/raw/orders.csv')
products_df = read_csv('data/raw/products.csv')
order_items_df = read_csv('data/raw/order_items.csv')
payments_df = read_csv('data/raw/payments.csv')


CUSTOMER_SCHEMA = [
    "customer_id",
    "first_name",
    "last_name",
    "gender",
    "email",
    "phone",
    "address",
    "city",
    "state",
    "signup_date"
]

# validate_schema(customers_df, CUSTOMER_SCHEMA)
print(customers_df)

validate_missing_values(customers_df)
# validate_duplicate_rows(customers_df)
# validate_duplicate_primary_keys(customers_df, 'customer_id')
validate_emails(customers_df, 'email')
validate_phone_numbers(customers_df, 'phone')
trim_whitespace(customers_df)
print(customers_df)