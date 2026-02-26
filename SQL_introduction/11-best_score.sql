-- Write a query to display the score and name of all records in second_table with a score higher than or equal to 10, ordered by score in descending order.
SELECT score, name
FROM second_table 
WHERE score >= 10
ORDER BY score DESC