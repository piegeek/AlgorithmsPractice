-- Subqueries and can't use aggregate functions in "WHERE" clause
-- My sol
SELECT firstname, surname, joindate
FROM CD.MEMBERS
WHERE joindate = (
  SELECT MAX(joindate)
  FROM CD.MEMBERS
  );