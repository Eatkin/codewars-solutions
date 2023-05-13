-- https://www.codewars.com/kata/59413d53f5c3947364000016
/*  SQL  */
SELECT regexp_split_to_table(text, '[aeiouAEIOU]') AS results
FROM random_string