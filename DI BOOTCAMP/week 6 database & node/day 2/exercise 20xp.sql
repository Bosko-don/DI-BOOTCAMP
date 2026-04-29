
-- =========================================
-- 1. CREATE TABLES (SIMPLIFIED VERSION)
-- =========================================

CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    create_date DATE DEFAULT CURRENT_DATE
);

CREATE TABLE film (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    release_year INT,
    rental_rate NUMERIC
);

CREATE TABLE address (
    address_id SERIAL PRIMARY KEY,
    address VARCHAR(100),
    phone VARCHAR(20),
    district VARCHAR(50)
);

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    customer_id INT,
    amount NUMERIC,
    payment_date DATE
);

CREATE TABLE city (
    city_id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    country_id INT
);

CREATE TABLE country (
    country_id SERIAL PRIMARY KEY,
    country VARCHAR(50)
);

CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    film_id INT
);

CREATE TABLE staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

-- =========================================
-- 2. INSERT SAMPLE DATA
-- =========================================

INSERT INTO customer (first_name, last_name)
VALUES 
('John','Doe'),
('Jane','Smith'),
('Alex','Brown');

INSERT INTO film (title, description, release_year, rental_rate)
VALUES 
('Spiderman','Hero movie',2002,2.99),
('Batman','Dark hero',2005,0.99),
('Avengers','Marvel team',2012,4.99);

INSERT INTO address (address, phone, district)
VALUES 
('123 Street','111-222','Texas'),
('456 Road','333-444','Nairobi');

INSERT INTO payment (customer_id, amount, payment_date)
VALUES 
(1, 10.00, '2026-01-01'),
(2, 20.00, '2026-01-02');

INSERT INTO country (country)
VALUES ('Kenya'), ('USA');

INSERT INTO city (city, country_id)
VALUES ('Nairobi',1), ('Dallas',2);

INSERT INTO inventory (film_id)
VALUES (1),(2);

INSERT INTO staff (first_name, last_name)
VALUES ('Mike','Boss'), ('Sara','Manager');

-- =========================================
-- 3. QUERIES (EXERCISE 2)
-- =========================================

-- All customers
SELECT * FROM customer;

-- Full name
SELECT first_name || ' ' || last_name AS full_name
FROM customer;

-- Unique create dates
SELECT DISTINCT create_date FROM customer;

-- Customers ordered DESC
SELECT * FROM customer ORDER BY first_name DESC;

-- Films ordered by rental rate
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- Address in Texas
SELECT address, phone
FROM address
WHERE district = 'Texas';

-- Film ID 1 or 2
SELECT * FROM film WHERE film_id IN (1,2);

-- Movie search
SELECT film_id, title, description, release_year, rental_rate
FROM film
WHERE title LIKE 'Sp%';

-- Cheapest films
SELECT * FROM film ORDER BY rental_rate ASC;

-- Join customer + payment
SELECT 
    c.customer_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id;

-- City + country
SELECT ci.city, co.country
FROM city ci
JOIN country co ON ci.country_id = co.country_id;

-- Staff sales
SELECT 
    s.staff_id,
    c.customer_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
JOIN staff s ON s.staff_id = 1;