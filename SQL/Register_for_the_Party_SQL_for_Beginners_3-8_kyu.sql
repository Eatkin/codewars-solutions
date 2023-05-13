-- https://www.codewars.com/kata/590cc86f7557c0494000007e
INSERT INTO participants ("name", age)
VALUES ('Ed', 31);

UPDATE participants
SET attending =
  CASE
    WHEN age >= 21 THEN
      true
    ELSE
      false
  END;
      

SELECT * FROM participants;
