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