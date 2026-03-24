-- My Sol
with bookings as (
	select mem.surname, mem.firstname, mem.memid, bkg.starttime
	from cd.members as mem
	inner join cd.bookings as bkg on mem.memid = bkg.memid
	where bkg.starttime > '2012-09-01'  
)

select surname, firstname, memid, min(starttime) from bookings group by surname, firstname, memid
order by memid;

-- Sol
select mems.surname, mems.firstname, mems.memid, min(bks.starttime) as starttime
	from cd.bookings bks
	inner join cd.members mems on
		mems.memid = bks.memid
	where starttime >= '2012-09-01'
	group by mems.surname, mems.firstname, mems.memid
order by mems.memid;      