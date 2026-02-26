-- Create a new table named second_table with specific columns and constraints
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256) NOT NULL,
	score INT NOT NULL,
);
INSERT INTO second_table VALUES (1, 'Alice', 85), (2, 'Bob', 90), (3, 'Charlie', 78);