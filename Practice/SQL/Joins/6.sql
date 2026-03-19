-- My Sol
-- Remark: Using case statements in WHERE clause
SELECT
mem.firstname || ' ' || mem.surname as member,
fac.name as facility,
CASE
	WHEN mem.memid = 0 THEN fac.guestcost * bkg.slots
	ELSE fac.membercost * bkg.slots
END AS cost
FROM
CD.MEMBERS AS mem
INNER JOIN CD.BOOKINGS AS bkg ON mem.memid = bkg.memid
INNER JOIN CD.FACILITIES AS fac ON fac.facid = bkg.facid
WHERE bkg.starttime >= '2012-09-14' AND bkg.starttime < '2012-09-15'
AND CASE
	WHEN mem.memid = 0 THEN fac.guestcost * bkg.slots
	ELSE fac.membercost * bkg.slots
END > 30
ORDER BY cost DESC;

-- Sol
select mems.firstname || ' ' || mems.surname as member, 
	facs.name as facility, 
	case 
		when mems.memid = 0 then
			bks.slots*facs.guestcost
		else
			bks.slots*facs.membercost
	end as cost
        from
                cd.members mems                
                inner join cd.bookings bks
                        on mems.memid = bks.memid
                inner join cd.facilities facs
                        on bks.facid = facs.facid
        where
		bks.starttime >= '2012-09-14' and 
		bks.starttime < '2012-09-15' and (
			(mems.memid = 0 and bks.slots*facs.guestcost > 30) or
			(mems.memid != 0 and bks.slots*facs.membercost > 30)
		)
order by cost desc;          