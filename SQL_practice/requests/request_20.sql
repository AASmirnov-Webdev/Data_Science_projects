WITH company_rais AS
  (SELECT i.company_id AS id,
          SUM(fr.raised_amount) AS sum_rais
   FROM investment AS i
   JOIN funding_round AS fr ON i.funding_round_id = fr.id
   GROUP BY i.company_id)
SELECT c1.name AS acquiring_company,
       a.price_amount,
       c2.name AS acquired_company,
       c2.funding_total,
       ROUND(a.price_amount/c2.funding_total) AS prop
FROM acquisition AS a
LEFT JOIN company AS c1 ON a.acquiring_company_id = c1.id
LEFT JOIN company AS c2 ON a.acquired_company_id = c2.id
LEFT JOIN company_rais ON a.acquired_company_id = company_rais.id
WHERE a.price_amount <> 0
  AND c2.funding_total <> 0
ORDER BY a.price_amount DESC,
         acquired_company
LIMIT 10;

--c2.funding_total,
--round(a.price_amount/c2.funding_total)
