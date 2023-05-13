-- https://www.codewars.com/kata/580918e24a85b05ad000010c
-- Create your SELECT statement here
SELECT people.*, COUNT(toys.id) AS toy_count
FROM toys JOIN people ON people.id = toys.people_id
GROUP BY people.id;