-- Group data
SELECT score, COUNT(score) AS number GROUP BY score ORDER BY number DESC;
