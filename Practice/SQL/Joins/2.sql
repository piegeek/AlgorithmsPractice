-- My Sol
SELECT starttime as start, name
FROM CD.BOOKINGS
INNER JOIN CD.FACILITIES ON CD.BOOKINGS.facid = CD.FACILITIES.facid
WHERE starttime > '2012-09-21' AND starttime < '2012-09-22'
AND name LIKE '%Tennis Court%'
ORDER BY starttime;

-- Remember: String matching uses "LIKE"

-- Sol
select bks.starttime as start, facs.name as name
	from 
		cd.facilities facs
		inner join cd.bookings bks
			on facs.facid = bks.facid
	where 
		facs.name in ('Tennis Court 2','Tennis Court 1') and
		bks.starttime >= '2012-09-21' and
		bks.starttime < '2012-09-22'
order by bks.starttime;  