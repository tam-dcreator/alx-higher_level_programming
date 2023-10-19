-- Script that lists the number of records with the same score
-- The number of records for the score would be labelled `number`
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
ORDER BY number DESC;
