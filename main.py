from src.extract.read_csv import read_csv
from src.validate.duplicates import validate_duplicate_rows, validate_duplicate_primary_keys
from src.validate.emails import validate_emails
from src.validate.missing import validate_missing_values
from src.validate.phone import validate_phone_numbers
from src.validate.schema import validate_schema
from src.tranform.standardize_case import standardize_case
from src.tranform.trim_whitespace import trim_whitespace
from src.tranform.convert_dtypes import convert_dtypes
from src.tranform.save_cleaned import save_cleaned
# from src.tranform.phone import phone
from src.load.load_customers import load_customers
# from src.load.load_orders import load_orders
from src.load.load_products import load_products

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

# ========== Function Calls ==========

# validate_schema(customers_df, CUSTOMER_SCHEMA)
# print(customers_df.dtypes)

# validate_missing_values(customers_df)
# validate_duplicate_rows(customers_df)
# validate_duplicate_primary_keys(customers_df, 'customer_id')
# validate_emails(customers_df, 'email')
# validate_phone_numbers(customers_df, 'phone')
# trim_whitespace(customers_df)
# standardize_case(customers_df)
# convert_dtypes(customers_df)
# # phone(customers_df)  #will make an update in version 2.0 to make it more robust and handle different phone number formats, including international numbers.
# print(customers_df.dtypes)
# save_cleaned(customers_df, 'data/cleaned/customers.csv')

# cleaned_customers_df = read_csv('data/cleaned/customers.csv')

# print("\nCleaned Customers DataFrame:")
# print(cleaned_customers_df)

# load_customers(cleaned_customers_df)
# print(customers_df)

# trim_whitespace(products_df)
# standardize_case(products_df)
# print(products_df)

# convert_dtypes(payments_df)

# print(payments_df)

# convert_dtypes(orders_df)
# save_cleaned(orders_df, 'data/cleaned/orders.csv')
# print(orders_df)

validate_missing_values(products_df)
validate_duplicate_rows(products_df)
validate_duplicate_primary_keys(products_df, 'product_id')
trim_whitespace(products_df)
convert_dtypes(products_df)
print(products_df.dtypes)
save_cleaned(products_df, 'data/cleaned/products.csv')
print(products_df.dtypes)
load_products(products_df)