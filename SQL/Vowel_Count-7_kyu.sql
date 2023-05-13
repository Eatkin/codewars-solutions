-- https://www.codewars.com/kata/54ff3102c1bad923760001f3
-- # write your SQL statement here: you are given a table 'getcount' with column 'str', return a table with column 'str' and your result in a column named 'res'.

SELECT str,
LENGTH(str) - LENGTH(REPLACE(str, 'a', ''))
+ LENGTH(str) - LENGTH(REPLACE(str, 'e', ''))
+ LENGTH(str) - LENGTH(REPLACE(str, 'i', ''))
+ LENGTH(str) - LENGTH(REPLACE(str, 'o', ''))
+ LENGTH(str) - LENGTH(REPLACE(str, 'u', ''))
AS res
FROM getcount