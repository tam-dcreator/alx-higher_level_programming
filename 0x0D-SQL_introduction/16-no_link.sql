-- Script that lists all records of the table with names
-- Records would be ordered by descending order of scores
SELECT score, name FROM second_table WHERE name != 'NULL' ORDER BY score DESC;
