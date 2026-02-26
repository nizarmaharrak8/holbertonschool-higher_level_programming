-- Write a query to display the score and the number of records with that score in second_table, ordered by the number of records in descending order.
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;