"""
Part2.py — extend the schema with products and order_items tables.
Adds to the SAME sql_learning.db that Part1.py created.
Run this AFTER Part1.py.
"""
import duckdb

# Connect to the same database file — this is the key point
con = duckdb.connect("sql_learning.db")

# Fresh start — drop the new tables if they already exist from a prior run
# (leaves customers and orders untouched)
con.execute("DROP TABLE IF EXISTS order_items")
con.execute("DROP TABLE IF EXISTS products")

# --- Create products ---
con.execute("""
    CREATE TABLE products (
        product_id   INTEGER,
        product_name VARCHAR,
        category     VARCHAR,
        price        DECIMAL(10,2)
    )
""")

con.execute("""
    INSERT INTO products VALUES
        (101, 'Wireless Headphones', 'Electronics',  80.00),
        (102, 'Yoga Mat',            'Fitness',      30.00),
        (103, 'Coffee Maker',        'Kitchen',     120.00),
        (104, 'Running Shoes',       'Fitness',     100.00),
        (105, 'Bluetooth Speaker',   'Electronics',  50.00),
        (106, 'Cookbook',            'Books',        25.00),
        (107, 'Desk Lamp',           'Home',         45.00)
""")

# --- Create order_items ---
con.execute("""
    CREATE TABLE order_items (
        order_id   INTEGER,
        product_id INTEGER,
        quantity   INTEGER
    )
""")

con.execute("""
    INSERT INTO order_items VALUES
        (1001, 101, 1), (1001, 106, 2),
        (1002, 103, 1),
        (1003, 101, 2), (1003, 105, 1),
        (1004, 102, 1),
        (1005, 104, 1), (1005, 103, 1),
        (1006, 105, 2),
        (1007, 106, 1),
        (1008, 101, 1), (1008, 104, 1),
        (1009, 102, 2),
        (1010, 105, 1),
        (1011, 103, 1), (1011, 104, 1),
        (1012, 106, 1)
""")

# --- Verify ---
print("--- All tables now in sql_learning.db ---")
con.sql("SHOW TABLES").show()

print("\n--- Row counts ---")
con.sql("""
    SELECT 'customers'   AS table_name, COUNT(*) AS row_count FROM customers
    UNION ALL
    SELECT 'orders',      COUNT(*) FROM orders
    UNION ALL
    SELECT 'products',    COUNT(*) FROM products
    UNION ALL
    SELECT 'order_items', COUNT(*) FROM order_items
    ORDER BY table_name
""").show()

# --- Prove the join works across all 4 tables ---
print("\n--- Proof of concept: 3-table join ---")
con.sql("""
    SELECT
        c.name       AS customer,
        p.product_name,
        oi.quantity
    FROM customers   c
    JOIN orders      o  ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id    = oi.order_id
    JOIN products    p  ON oi.product_id = p.product_id
    ORDER BY c.name, p.product_name
    LIMIT 5
""").show()

con.close()