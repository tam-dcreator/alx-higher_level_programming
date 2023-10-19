-- Script that lists all records of `second_table` with score >= 10
-- Records are ordered in descending order of scores
SELECT score, name FROM second_table WHERE score >= '10' ORDER BY score DESC;
