CREATE TABLE products (
    product_id   INTEGER,
    product_name VARCHAR,
    category     VARCHAR,
    price        DECIMAL(10,2)
);

INSERT INTO products VALUES
    (101, 'Wireless Headphones', 'Electronics', 80.00),
    (102, 'Yoga Mat',            'Fitness',     30.00),
    (103, 'Coffee Maker',        'Kitchen',    120.00),
    (104, 'Running Shoes',       'Fitness',    100.00),
    (105, 'Bluetooth Speaker',   'Electronics', 50.00),
    (106, 'Cookbook',            'Books',       25.00),
    (107, 'Desk Lamp',           'Home',        45.00);  -- never ordered

CREATE TABLE order_items (
    order_id   INTEGER,
    product_id INTEGER,
    quantity   INTEGER
);