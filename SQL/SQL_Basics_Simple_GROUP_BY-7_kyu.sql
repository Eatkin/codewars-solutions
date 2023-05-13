-- https://www.codewars.com/kata/58111f4ee10b5301a7000175
-- Create your SELECT statement here
SELECT age, COUNT(age) AS people_count
FROM people
GROUP BY age;