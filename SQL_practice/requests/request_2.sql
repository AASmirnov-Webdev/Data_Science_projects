SELECT funding_total
FROM company
WHERE category_code = 'news'
      AND country_code = 'USA'
--GROUP BY name
ORDER BY funding_total DESC
