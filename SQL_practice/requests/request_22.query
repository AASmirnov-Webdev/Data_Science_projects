SELECT t1.month,
       t1.count_f,
       t2.count_c,
       t2.sum_amount
FROM
  (SELECT extract(MONTH
                  FROM fr.funded_at) AS MONTH,
          count(DISTINCT f.name) AS count_f
   FROM funding_round AS fr
   LEFT JOIN investment AS i ON i.funding_round_id = fr.id
   LEFT JOIN fund AS f ON i.fund_id = f.id
   WHERE extract(YEAR
                 FROM fr.funded_at) BETWEEN 2010 AND 2013
     AND f.country_code = 'USA'
   GROUP BY extract(MONTH
                    FROM fr.funded_at)) AS t1
INNER JOIN
  (SELECT extract(MONTH
                  FROM acquired_at) AS MONTH,
          count(id) AS count_c,
          sum(price_amount) AS sum_amount
   FROM acquisition
   WHERE extract(YEAR
                 FROM acquired_at) BETWEEN 2010 AND 2013
   GROUP BY extract(MONTH
                    FROM acquired_at)) AS t2 ON t1.month = t2.month         
