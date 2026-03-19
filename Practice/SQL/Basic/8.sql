-- My sol
SELECT memid, surname, firstname, joindate FROM CD.MEMBERS
WHERE joindate > '2012-09-01 00:00:00';

-- Sol
select memid, surname, firstname, joindate 
	from cd.members
	where joindate >= '2012-09-01';     