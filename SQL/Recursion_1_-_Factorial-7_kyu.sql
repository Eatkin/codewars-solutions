-- https://www.codewars.com/kata/5694cb0ec554589633000036
-- create recursively the table with n up to and including 16
WITH RECURSIVE factorial(n, value) AS (
  SELECT 0, 1::BIGINT -- Initial values
  UNION ALL
  SELECT n + 1, (n + 1) * value -- Recursive step
  FROM factorial
  WHERE n < 16
)
SELECT n, value AS fact
FROM factorial;
