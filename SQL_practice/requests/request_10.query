SELECT country_code,
        MIN(invested_companies) AS min,
        MAX(invested_companies) AS max,
        AVG(invested_companies) AS avg
FROM fund
WHERE EXTRACT(YEAR FROM CAST(founded_at AS date)) BETWEEN '2010' AND '2012'
GROUP BY country_code
    HAVING MIN(invested_companies) != 0
ORDER BY avg DESC
LIMIT 10
