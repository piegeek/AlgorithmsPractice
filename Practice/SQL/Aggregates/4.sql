-- My Sol
select fac.facid, sum(bkg.slots)
from cd.facilities as fac
inner join cd.bookings as bkg on bkg.facid = fac.facid
group by fac.facid
order by fac.facid;

-- Sol
select facid, sum(slots) as "Total Slots"
	from cd.bookings
	group by facid
order by facid; 