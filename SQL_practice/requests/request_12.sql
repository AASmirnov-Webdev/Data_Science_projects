SELECT com.name AS company_name,
       COUNT( DISTINCT edu.instituition) AS edu_count
FROM company AS com
JOIN people AS pep ON com.id = pep.company_id
JOIN education AS edu ON edu.person_id = pep.id
GROUP BY company_name
ORDER BY edu_count DESC
LIMIT 5;
