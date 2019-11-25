-- Lists all records with a score >= 10 in second_table
-- Records should be ordered by socres top first
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
