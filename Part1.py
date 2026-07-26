import duckdb

# Connect to a file-based DuckDB database so your tables persist
# between runs (in-memory would forget everything when the script ends)
con = duckdb.connect("sql_learning.db")

# --- Sanity check ---
con.sql("SELECT 'hello duckdb' AS greeting").show()

# --- Fresh start: drop tables if they already exist from a prior run ---
con.execute("DROP TABLE IF EXISTS orders")
con.execute("DROP TABLE IF EXISTS customers")

# --- Create the customers table ---
# Notice: the ENTIRE SQL statement is inside a triple-quoted string.
# Triple quotes let you write multi-line strings without escaping newlines.
con.execute("""
    CREATE TABLE customers (
        customer_id INTEGER,
        name        VARCHAR,
        email       VARCHAR,
        country     VARCHAR,
        signup_date DATE
    )
""")

con.execute("""
    INSERT INTO customers VALUES
        (1, 'Alice',   'alice@x.com',   'USA',    '2024-01-15'),
        (2, 'Bob',     'bob@x.com',     'USA',    '2024-02-03'),
        (3, 'Diana',   NULL,            'Canada', '2024-03-20'),
        (4, 'Eve',     'eve@x.com',     'UK',     '2024-03-25'),
        (5, 'Frank',   'frank@x.com',   'USA',    '2024-04-10'),
        (6, 'Grace',   'grace@x.com',   'UK',     '2024-04-18'),
        (7, 'Henry',   NULL,            'Canada', '2024-05-02')
""")

# --- Create the orders table ---
con.execute("""
    CREATE TABLE orders (
        order_id    INTEGER,
        customer_id INTEGER,
        amount      DECIMAL(10,2),
        order_date  DATE
    )
""")

con.execute("""
    INSERT INTO orders VALUES
        (1001, 1,  50.00, '2024-01-20'),
        (1002, 2,  75.00, '2024-02-05'),
        (1003, 1, 200.00, '2024-02-10'),
        (1004, 3,  30.00, '2024-03-22'),
        (1005, 1, 150.00, '2024-04-01'),
        (1006, 4,  90.00, '2024-04-15'),
        (1007, 5,  45.00, '2024-04-20'),
        (1008, 2, 110.00, '2024-04-25'),
        (1009, 6,  60.00, '2024-05-01'),
        (1010, 1,  80.00, '2024-05-05'),
        (1011, 4, 200.00, '2024-05-08'),
        (1012, 5,  25.00, '2024-05-12')
""")

# --- Verify with SELECT queries ---
# .sql() returns a result object; .show() prints it as a nice table
print("\n--- customers count ---")
con.sql("SELECT COUNT(*) AS customers_count FROM customers").show()

print("\n--- orders count ---")
con.sql("SELECT COUNT(*) AS orders_count FROM orders").show()

print("\n--- first 5 customers ---")
con.sql("SELECT * FROM customers LIMIT 5").show()

# Always close the connection when done (good hygiene)
con.close()