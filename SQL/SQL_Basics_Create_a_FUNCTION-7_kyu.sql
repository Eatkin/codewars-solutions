-- https://www.codewars.com/kata/580fe518cefeff16d00000c0
CREATE FUNCTION increment_by_one(num INT)
RETURNS INT
AS
$$
  SELECT num + 1;
$$
LANGUAGE SQL;