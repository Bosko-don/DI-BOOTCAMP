
-- =========================================
-- 🌟 CREATE MINI DVD DATABASE (SELF CONTAINED)
-- =========================================

DROP TABLE IF EXISTS film CASCADE;
DROP TABLE IF EXISTS language CASCADE;
DROP TABLE IF EXISTS customer CASCADE;
DROP TABLE IF EXISTS rental CASCADE;
DROP TABLE IF EXISTS payment CASCADE;
DROP TABLE IF EXISTS actor CASCADE;
DROP TABLE IF EXISTS film_actor CASCADE;
DROP TABLE IF EXISTS inventory CASCADE;

-- =========================================
-- TABLES
-- =========================================

CREATE TABLE language (
    language_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE film (
    film_id SERIAL PRIMARY KEY,
    title VARCHAR(100),
    description TEXT,
    length INT,
    rental_rate NUMERIC,
    language_id INT
);

CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE rental (
    rental_id SERIAL PRIMARY KEY,
    customer_id INT,
    rental_date DATE,
    return_date DATE
);

CREATE TABLE payment (
    payment_id SERIAL PRIMARY KEY,
    customer_id INT,
    amount NUMERIC,
    payment_date DATE
);

CREATE TABLE actor (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50)
);

CREATE TABLE film_actor (
    film_id INT,
    actor_id INT
);

CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,
    film_id INT
);

-- =========================================
-- INSERT DATA
-- =========================================

INSERT INTO language (name) VALUES
('English'),
('French'),
('Spanish');

INSERT INTO film (title, description, length, rental_rate, language_id) VALUES
('Sumo Champion', 'Story about a sumo wrestler', 120, 4.99, 1),
('Deep Ocean', 'Short documentary under water', 55, 2.99, 1),
('Boat Adventure', 'A journey on a dangerous boat', 140, 5.99, 2);

INSERT INTO customer (first_name, last_name) VALUES
('Matthew','Mahan'),
('Penelope','Monroe'),
('John','Doe');

INSERT INTO actor (first_name, last_name) VALUES
('PENELOPE','MONROE'),
('MATTHEW','MAHAN');

INSERT INTO film_actor VALUES
(1,1),
(3,2);

INSERT INTO rental (customer_id, rental_date, return_date) VALUES
(1,'2005-07-29','2005-07-30'),
(1,'2005-07-28','2005-08-01');

INSERT INTO payment (customer_id, amount, payment_date) VALUES
(1,5.00,'2005-07-29'),
(1,6.00,'2005-07-30'),
(2,3.00,'2005-07-28');

INSERT INTO inventory (film_id) VALUES (1),(2),(3);

-- =========================================
-- 🌟 EXERCISE 1 QUERIES
-- =========================================

-- 1. All languages
SELECT * FROM language;

-- 2. Films with language
SELECT f.title, f.description, l.name AS language_name
FROM film f
JOIN language l ON f.language_id = l.language_id;

-- 3. All languages even if no films
SELECT f.title, f.description, l.name
FROM language l
LEFT JOIN film f ON f.language_id = l.language_id;

-- 4. new_film table
CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

INSERT INTO new_film (name) VALUES ('Film A'), ('Film B');

-- 5. customer_review
CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INT REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INT REFERENCES language(language_id),
    title VARCHAR(100),
    score INT,
    review_text TEXT,
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text)
VALUES (1,1,'Great Film',9,'Amazing!'),
       (2,1,'Nice Watch',8,'Good story');

-- Delete test
DELETE FROM new_film WHERE id = 1;

-- =========================================
-- 🌟 EXERCISE 2 QUERIES
-- =========================================

-- Update language
UPDATE film SET language_id = 2 WHERE film_id = 1;

-- Outstanding rentals
SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

-- Expensive outstanding movies
SELECT f.title, f.rental_rate
FROM film f
JOIN inventory i ON f.film_id = i.film_id
JOIN rental r ON r.customer_id = 1
WHERE r.return_date IS NULL
ORDER BY f.rental_rate DESC;

-- Find movies (friend tasks)

-- 1 sumo + penelope
SELECT f.title
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.description ILIKE '%sumo%'
AND a.first_name = 'PENELOPE';

-- 2 short documentary R (simplified)
SELECT * FROM film WHERE length < 60;

-- 3 Matthew Mahan expensive rental
SELECT *
FROM rental r
JOIN payment p ON r.customer_id = p.customer_id
JOIN customer c ON c.customer_id = r.customer_id
WHERE c.first_name = 'Matthew'
AND p.amount > 4
AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

-- 4 boat movie
SELECT * FROM film
WHERE title ILIKE '%boat%' OR description ILIKE '%boat%';
