-- 5. Unique id
-- Create a table with the id and name of a force. The id should be unique.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);