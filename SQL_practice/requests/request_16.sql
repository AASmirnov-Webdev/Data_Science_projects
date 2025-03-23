WITH comp AS
  (SELECT DISTINCT id
   FROM company
   WHERE status='closed'
     AND id in
       (SELECT company_id
        FROM funding_round
        WHERE is_first_round=1
          AND is_last_round=1))
SELECT p.id,
       count(e.instituition)
FROM people AS p
JOIN education AS e ON e.person_id=p.id
WHERE company_id in
    (SELECT *
     FROM comp)
GROUP BY p.id
