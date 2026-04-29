
-- =========================================
-- 1. CREATE TABLES
-- =========================================

CREATE TABLE FirstTab (
    id INTEGER,
    name VARCHAR(10)
);

CREATE TABLE SecondTab (
    id INTEGER
);

-- =========================================
-- 2. INSERT DATA
-- =========================================

INSERT INTO FirstTab VALUES
(5,'Pawan'),
(6,'Sharlee'),
(7,'Krish'),
(NULL,'Avtaar');

INSERT INTO SecondTab VALUES
(5),
(NULL);

-- =========================================
-- 3. VIEW TABLES (OPTIONAL CHECK)
-- =========================================

SELECT * FROM FirstTab;

SELECT * FROM SecondTab;

-- =========================================
-- 4. QUESTIONS + EXECUTION RESULTS
-- =========================================

-- Q1
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NULL
);
-- RESULT: 0

-- Q2
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id = 5
);
-- RESULT: 2

-- Q3
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab
);
-- RESULT: 0

-- Q4
SELECT COUNT(*) 
FROM FirstTab AS ft 
WHERE ft.id NOT IN (
    SELECT id FROM SecondTab WHERE id IS NOT NULL
);
-- RESULT: 2