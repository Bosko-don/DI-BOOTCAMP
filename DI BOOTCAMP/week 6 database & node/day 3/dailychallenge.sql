
-- =========================================
-- 🌟 SAFE RESET (NO ERRORS)
-- =========================================

DROP TABLE IF EXISTS library CASCADE;
DROP TABLE IF EXISTS student CASCADE;
DROP TABLE IF EXISTS book CASCADE;
DROP TABLE IF EXISTS customer_profile CASCADE;
DROP TABLE IF EXISTS customer CASCADE;

-- =========================================
-- 🌟 PART I: ONE TO ONE RELATIONSHIP
-- =========================================

-- 1. CUSTOMER TABLE
CREATE TABLE customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- 2. CUSTOMER PROFILE TABLE
CREATE TABLE customer_profile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INT UNIQUE REFERENCES customer(id) ON DELETE CASCADE
);

-- =========================================
-- INSERT CUSTOMERS
-- =========================================

INSERT INTO customer (first_name, last_name)
VALUES 
('John','Doe'),
('Jerome','Lalu'),
('Lea','Rive');

-- =========================================
-- INSERT PROFILES (USING SUBQUERIES)
-- =========================================

INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
    TRUE,
    (SELECT id FROM customer WHERE first_name = 'John')
);

INSERT INTO customer_profile (isLoggedIn, customer_id)
VALUES (
    FALSE,
    (SELECT id FROM customer WHERE first_name = 'Jerome')
);

-- =========================================
-- PART I QUERIES (JOINS)
-- =========================================

-- 1. Logged-in customers
SELECT c.first_name
FROM customer c
JOIN customer_profile cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

-- 2. All customers + login status
SELECT c.first_name, cp.isLoggedIn
FROM customer c
LEFT JOIN customer_profile cp
ON c.id = cp.customer_id;

-- 3. Number of NOT logged-in customers
SELECT COUNT(*)
FROM customer c
LEFT JOIN customer_profile cp
ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn IS NULL;

-- =========================================
-- 🌟 PART II: BOOK + STUDENT + LIBRARY
-- =========================================

-- 1. BOOK TABLE
CREATE TABLE book (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author VARCHAR(100) NOT NULL
);

-- 2. STUDENT TABLE (AGE CONSTRAINT)
CREATE TABLE student (
    student_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    age INT CHECK (age <= 15)
);

-- 3. LIBRARY JUNCTION TABLE
CREATE TABLE library (
    book_fk_id INT,
    student_fk_id INT,
    borrowed_date DATE,
    PRIMARY KEY (book_fk_id, student_fk_id),
    FOREIGN KEY (book_fk_id) REFERENCES book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (student_fk_id) REFERENCES student(student_id) ON DELETE CASCADE ON UPDATE CASCADE
);

-- =========================================
-- INSERT BOOKS
-- =========================================

INSERT INTO book (title, author)
VALUES 
('Alice In Wonderland','Lewis Carroll'),
('Harry Potter','J.K Rowling'),
('To kill a mockingbird','Harper Lee');

-- =========================================
-- INSERT STUDENTS
-- =========================================

INSERT INTO student (name, age)
VALUES 
('John',12),
('Lera',11),
('Patrick',10),
('Bob',14);

-- =========================================
-- INSERT BORROW RECORDS (SUBQUERIES)
-- =========================================

INSERT INTO library VALUES (
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'John'),
    '2022-02-15'
);

INSERT INTO library VALUES (
    (SELECT book_id FROM book WHERE title = 'To kill a mockingbird'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-03-03'
);

INSERT INTO library VALUES (
    (SELECT book_id FROM book WHERE title = 'Alice In Wonderland'),
    (SELECT student_id FROM student WHERE name = 'Lera'),
    '2021-05-23'
);

INSERT INTO library VALUES (
    (SELECT book_id FROM book WHERE title = 'Harry Potter'),
    (SELECT student_id FROM student WHERE name = 'Bob'),
    '2021-08-12'
);

-- =========================================
-- DISPLAY DATA
-- =========================================

-- 1. All library data
SELECT * FROM library;

-- 2. Student names + book titles
SELECT 
    s.name,
    b.title
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id;

-- 3. Average age of students who borrowed Alice
SELECT AVG(s.age)
FROM library l
JOIN student s ON l.student_fk_id = s.student_id
JOIN book b ON l.book_fk_id = b.book_id
WHERE b.title = 'Alice In Wonderland';

-- =========================================
-- DELETE TEST (CASCADE CHECK)
-- =========================================

DELETE FROM student WHERE name = 'John';

-- RESULT:
-- John's records in library are automatically deleted
-- because ON DELETE CASCADE is active