-- 1. All customers
SELECT * FROM customers;

-- 2. Just names and emails
SELECT name, email FROM customers;

-- 3. Customers from the USA
SELECT name, country FROM customers WHERE country = 'USA';

-- 4. Customers who signed up after March 1st
SELECT name, signup_date FROM customers WHERE signup_date > '2024-03-01';

-- 5. Customers with no email recorded
SELECT name FROM customers WHERE email IS NULL;

-- 6. Customers ordered by signup date (newest first)
SELECT name, signup_date FROM customers ORDER BY signup_date DESC;

-- 7. The 3 most recent customers
SELECT name, signup_date FROM customers ORDER BY signup_date DESC LIMIT 3;

-- 8. The 3 largest orders
SELECT order_id, amount FROM orders ORDER BY amount DESC LIMIT 3;

-- 9. Distinct countries represented
SELECT DISTINCT country FROM customers;

-- 10. Orders sorted by date, then amount descending
SELECT order_id, order_date, amount FROM orders ORDER BY order_date, amount DESC;

-- 11. Total number of orders
SELECT COUNT(*) AS num_orders FROM orders;

-- 12. Total revenue across all orders
SELECT SUM(amount) AS total_revenue FROM orders;

-- 13. Largest, smallest, and average order value
SELECT
    MAX(amount) AS biggest,
    MIN(amount) AS smallest,
    AVG(amount) AS average
FROM orders;

-- 14. How many customers have a NULL email?
SELECT
    COUNT(*)       AS total_customers,
    COUNT(email)   AS with_email,
    COUNT(*) - COUNT(email) AS missing_email
FROM customers;

-- 15. How many distinct customers placed orders?
SELECT COUNT(DISTINCT customer_id) AS active_customers FROM orders;

-- 16. Total spent per customer
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC;

-- 17. Number of orders per customer
SELECT customer_id, COUNT(*) AS num_orders
FROM orders
GROUP BY customer_id
ORDER BY num_orders DESC;

-- 18. Customers from each country
SELECT country, COUNT(*) AS num_customers
FROM customers
GROUP BY country
ORDER BY num_customers DESC;

-- 19. Customers who spent more than $200 in total
SELECT customer_id, SUM(amount) AS total_spent
FROM orders
GROUP BY customer_id
HAVING SUM(amount) > 200
ORDER BY total_spent DESC;

-- 20. Per-customer order stats: count, total, average, biggest single order
SELECT
    customer_id,
    COUNT(*)      AS num_orders,
    SUM(amount)   AS total_spent,
    AVG(amount)   AS avg_order_value,
    MAX(amount)   AS biggest_order
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC;