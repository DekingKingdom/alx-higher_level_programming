-- Show records with same values
-- SELECT number of records with same score in sorted order
SELECT score,COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY score DESC;
