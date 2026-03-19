-- My Sol
SELECT starttime
FROM 
CD.MEMBERS 
INNER JOIN CD.BOOKINGS ON CD.MEMBERS.memid = CD.BOOKINGS.memid
INNER JOIN CD.FACILITIES ON CD.BOOKINGS.facid = CD.FACILITIES.facid
WHERE firstname = 'David' AND surname = 'Farrell';

-- Learn about Inner Join, Left Join, Right Join

-- Sol
select bks.starttime 
	from 
		cd.bookings bks
		inner join cd.members mems
			on mems.memid = bks.memid
	where 
		mems.firstname='David' 
		and mems.surname='Farrell';  