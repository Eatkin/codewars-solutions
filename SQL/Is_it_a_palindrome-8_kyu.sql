-- https://www.codewars.com/kata/57a1fd2ce298a731b20006a4
-- # write your SQL statement here: you are given a table 'ispalindrome' with column 'str', return a table with column 'str' and your result in a column named 'res'.
SELECT str, LOWER(str) = REVERSE(LOWER(str)) as res FROM ispalindrome