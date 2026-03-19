-- IN Operator
SELECT * FROM CD.FACILITIES
WHERE facid IN (1, 5)

-- How to do it with OR operator
SELECT * FROM CD.FACILITIES
WHERE facid = 1 OR facid = 5