-- 🌟 Exercise 1: Items and Customers

-- 1. All items ordered by price (lowest → highest)
SELECT *
FROM items
ORDER BY price ASC;

-- 2. Items with price >= 80 (highest → lowest)
SELECT *
FROM items
WHERE price >= 80
ORDER BY price DESC;

-- 3. First 3 customers ordered by first name (A–Z), excluding primary key
SELECT first_name, last_name
FROM customers
ORDER BY first_name ASC
LIMIT 3;

-- 4. All last names only (Z–A)
SELECT last_name
FROM customers
ORDER BY last_name DESC;