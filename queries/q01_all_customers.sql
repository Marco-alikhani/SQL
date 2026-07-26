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