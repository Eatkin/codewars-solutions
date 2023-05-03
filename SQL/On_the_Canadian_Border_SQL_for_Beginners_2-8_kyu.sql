-- /kata/590ba881fe13cfdcc20001b4
SELECT * FROM travelers
WHERE NOT (country = 'Canada' OR country = 'Mexico' OR country = 'USA');