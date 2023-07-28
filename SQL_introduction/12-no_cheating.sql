-- This script updates Bob! Well, not Bob, but their score in the second_table.
UPDATE second_table(
	SET score = 10
	WHERE name = "Bob"
);