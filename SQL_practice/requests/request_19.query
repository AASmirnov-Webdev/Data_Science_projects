SELECT f.name AS name_of_fund,
       c.name AS name_of_company,
       fr.raised_amount AS amount
FROM investment AS i
LEFT JOIN company AS c ON c.id = i.company_id
LEFT JOIN fund AS f ON f.id = i.fund_id
INNER JOIN funding_round AS fr ON fr.id = i.funding_round_id
WHERE c.milestones > 6
  AND extract(YEAR
              FROM fr.funded_at) BETWEEN 2012 AND 2013
