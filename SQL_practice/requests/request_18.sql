SELECT AVG(qt)
FROM (SELECT DISTINCT p.id,
             COUNT(e.instituition) AS qt
     FROM people AS p INNER JOIN education AS e ON p.id = e.person_id
     WHERE company_id IN
         (SELECT DISTINCT id
          FROM company
          WHERE name = 'Facebook')
      GROUP BY p.id) AS res
