-- This one lists all records with a score smaller or equal than 10 inside the second_table of the database.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;