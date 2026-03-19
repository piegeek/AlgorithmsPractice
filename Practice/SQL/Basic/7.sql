SELECT name, 
-- This is new column
CASE
	WHEN monthlymaintenance > 100 THEN 'expensive'
	ELSE 'cheap'
END AS cost
-- This is new column
FROM CD.FACILITIES;
-- End with semicolon