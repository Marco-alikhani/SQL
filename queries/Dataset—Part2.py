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


INSERT INTO order_items VALUES
    (1001, 101, 1),
    (1001, 106, 2),
    (1002, 103, 1),
    (1003, 101, 2),
    (1003, 105, 1),
    (1004, 102, 1),
    (1005, 104, 1),
    (1005, 103, 1),
    (1006, 105, 2),
    (1007, 106, 1),
    (1008, 101, 1),
    (1008, 104, 1),
    (1009, 102, 2),
    (1010, 105, 1),
    (1011, 103, 1),
    (1011, 104, 1),
    (1012, 106, 1);

-- verify
SELECT COUNT(*) AS products_count    FROM products;    -- 7
SELECT COUNT(*) AS line_items_count  FROM order_items; -- 17