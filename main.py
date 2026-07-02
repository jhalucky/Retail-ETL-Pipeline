from src.extract.read_csv import read_csv

customers_df =  read_csv('data/raw/customers.csv')

print(customers_df.head())