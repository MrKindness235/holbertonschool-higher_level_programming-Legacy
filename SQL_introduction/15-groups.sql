-- This one is rather simple:
-- it lists all records with same score from second_table.
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY DESC;