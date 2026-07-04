TRUNCATE TABLE
order_items,
payments,
orders,
products,
customers
CASCADE;

psql -U postgres -d retail_db -f sql/truncate_tables.sql


