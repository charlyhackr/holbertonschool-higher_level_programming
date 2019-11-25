-- Lists all records of the second_table
-- records should be listed by descending score
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
