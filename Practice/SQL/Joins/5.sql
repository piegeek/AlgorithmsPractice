-- My Sol
SELECT 
DISTINCT 
mem.firstname || ' ' || mem.surname AS member,
fac.name AS facility
FROM
CD.MEMBERS AS mem 
INNER JOIN CD.BOOKINGS AS bkg ON bkg.memid = mem.memid
INNER JOIN CD.FACILITIES AS fac ON bkg.facid = fac.facid
WHERE fac.name LIKE '%Tennis Court%'
ORDER BY (mem.firstname || ' ' || mem.surname), fac.name;