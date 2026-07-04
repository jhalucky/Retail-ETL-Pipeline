CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(20),
    email VARCHAR(200) UNIQUE,
    phone VARCHAR(15) UNIQUE,
    address VARCHAR(200),
    city VARCHAR(100),
    state VARCHAR(100),
    signup_date DATE
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(100),
    brand VARCHAR(100),
    price DECIMAL(10,2),
    stock_quantity INT
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERNCES customers(customer_id),
    order_date DATE,
    order_status VARCHAR(50),
    total_amount DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_items_id INT PRIMARY KEY,
    order_id INT,
    customer_id INT,
    quantity INT,
    unit_price DECIMAL(10,2),

    FOREIGN KEY(order_id) REFERNCES orders(order_id),
    FOREIGN KEY(customer_id) REFERNCES customers(customer_id)

);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_method VARCHAR(50),
    payment_status VARCHAR(20),
    payment_date DATE,

    FOREIGN KEY(order_id) REFERNCES orders(order_id)
);