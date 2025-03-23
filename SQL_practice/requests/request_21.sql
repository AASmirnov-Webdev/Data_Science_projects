SELECT com.name,
       EXTRACT(month from fr.funded_at) as month
FROM company AS com
LEFT OUTER JOIN funding_round AS fr ON com.id = fr.company_id
WHERE com.category_code = 'social'
      AND EXTRACT(YEAR FROM CAST(fr.funded_at AS date)) BETWEEN '2010' AND '2013'
