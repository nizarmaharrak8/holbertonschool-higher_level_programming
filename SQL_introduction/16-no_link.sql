-- Write a query to display the score and name of all records in second_table where the name is not NULL and not an empty string, ordered by score in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;