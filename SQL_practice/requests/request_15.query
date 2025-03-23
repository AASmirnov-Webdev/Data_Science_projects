WITH closed_companies_list AS (SELECT DISTINCT c.id
                               FROM company AS c
                               LEFT JOIN funding_round AS fr ON c.id = fr.company_id
                               WHERE c.status = 'closed'
                               AND fr.is_first_round = 1
                               AND fr.is_last_round = 1),
 
     people_list AS (SELECT DISTINCT p.id
                     FROM closed_companies_list AS closed
                     JOIN people AS p ON closed.id = p.company_id),
 
     people_instituition_list AS (SELECT DISTINCT pl.id,
                                         e.instituition
                                  FROM people_list AS pl
                                  JOIN education AS e ON pl.id = e.person_id)
 
SELECT *
FROM people_instituition_list
