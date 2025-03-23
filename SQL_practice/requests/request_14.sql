WITH closed_companies_list AS (SELECT DISTINCT c.id
                               FROM company AS c
                               JOIN funding_round AS fr ON c.id = fr.company_id
                               WHERE c.status = 'closed'
                               AND fr.is_first_round = 1
                               AND fr.is_last_round = 1),
 
     people_list AS (SELECT DISTINCT p.id
                     FROM closed_companies_list AS closed
                     JOIN people AS p ON closed.id = p.company_id)

SELECT id
FROM people_list;
