-- 1. Every line item with full context: customer, order date, product, quantity, line total
SELECT
    c.name              AS customer,
    o.order_date,
    p.product_name,
    oi.quantity,
    oi.quantity * p.price AS line_total
FROM customers c
INNER JOIN orders      o  ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id    = oi.order_id
INNER JOIN products    p  ON oi.product_id = p.product_id
ORDER BY o.order_date, c.name;

-- 2. All customers with their total spending (zeros included)
SELECT
    c.name,
    COALESCE(SUM(o.amount), 0) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY total_spent DESC;

-- 3. Products that have NEVER been ordered
SELECT p.product_name, p.category
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_id IS NULL;

-- 4. Revenue per product category
SELECT
    p.category,
    SUM(oi.quantity * p.price) AS category_revenue,
    COUNT(DISTINCT oi.order_id) AS orders_touching_category
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY category_revenue DESC;

-- 5. Each customer's favorite category (highest spend)
-- (preview of harder analytical patterns — we'll do this cleaner in Chat 3 with window functions)
SELECT
    c.name,
    p.category,
    SUM(oi.quantity * p.price) AS category_spend
FROM customers c
INNER JOIN orders      o  ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id    = oi.order_id
INNER JOIN products    p  ON oi.product_id = p.product_id
GROUP BY c.name, p.category
ORDER BY c.name, category_spend DESC;

-- 6. Self-join — pairs of customers from the same country
SELECT
    a.name AS customer_a,
    b.name AS customer_b,
    a.country
FROM customers a
INNER JOIN customers b
        ON a.country = b.country
       AND a.customer_id < b.customer_id
ORDER BY a.country;