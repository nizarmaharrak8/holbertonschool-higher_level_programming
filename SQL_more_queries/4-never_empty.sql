-- 4. Never empty
-- Create a table with the id and name of a force. The id should never be null
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);