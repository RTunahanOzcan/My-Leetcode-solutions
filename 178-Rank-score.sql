SELECT 
    s.score,
    (SELECT COUNT(DISTINCT t.score)
     FROM Scores t
     WHERE t.score >= s.score) AS 'rank'
FROM Scores s
ORDER BY s.score DESC;

