from src.extract.read_csv import read_csv
from src.validate.validator import validate_missing_values, validate_duplicate_rows
customers_df =  read_csv('data/raw/customers.csv')

validate_missing_values(customers_df)
validate_duplicate_rows(customers_df)