-- https://www.codewars.com/kata/5861d28f124b35723e00005e
--# write your SQL statement here: you are given a table 'zerofuel' with columns 'distance_to_pump', 'mpg' and 'fuel_left', return a table with all the columns and your result in a column named 'res'.

SELECT distance_to_pump, mpg, fuel_left,
  CASE 
  WHEN mpg * fuel_left >= distance_to_pump THEN
    true
  ELSE
    false
  END as res
FROM zerofuel