-- Write a script that creates a new table called second_table with the following columns:
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256) NOT NULL,
	score INT NOT NULL,
);
INSERT INTO Second_table (id, name, score) VALUES
(1, 'John', 10), 
(2, 'Alex', 3),
(3, 'Bob', 14)
(4, 'George', 8)
;