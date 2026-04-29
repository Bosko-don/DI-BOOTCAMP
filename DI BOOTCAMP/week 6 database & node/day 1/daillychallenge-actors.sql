-- 1. Reset table
DROP TABLE IF EXISTS actors;

-- 2. Create table
CREATE TABLE actors (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    age DATE NOT NULL,
    number_oscars SMALLINT NOT NULL
);

-- 3. Insert initial data
INSERT INTO actors (first_name, last_name, age, number_oscars) VALUES
('Angelina', 'Jolie', '1975-06-04', 1),
('George', 'Clooney', '1961-05-06', 2),
('Jennifer', 'Aniston', '1969-02-11', 0),
('Matt', 'Damon', '1970-10-08', 5);

-- 4. Count actors
SELECT COUNT(*) AS total_actors FROM actors;

-- 5. Demonstrate failed insert safely (DO block catches error)
DO $$
BEGIN
    BEGIN
        INSERT INTO actors (first_name, last_name, age, number_oscars)
        VALUES (NULL, NULL, NULL, NULL);
    EXCEPTION
        WHEN others THEN
            RAISE NOTICE 'Insert failed as expected due to NOT NULL constraint.';
    END;
END $$;

-- 6. Correct insert
INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES ('Brad', 'Pitt', '1963-12-18', 2);

-- 7. Show all actors
SELECT * FROM actors;