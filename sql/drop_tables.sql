DROP TABLE IF EXISTS
order_items,
payments,
orders,
products,
customers
CASCADE;

psql -U postgres -d retail_db -f sql/drop_tables.sql