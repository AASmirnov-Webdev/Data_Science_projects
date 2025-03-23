SELECT pep.first_name,
       pep.last_name,
       edu.instituition
FROM people AS pep
LEFT OUTER JOIN education AS edu ON pep.id = edu.person_id
