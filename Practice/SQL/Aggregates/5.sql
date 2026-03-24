-- My Sol
select bkg.facid, sum(bkg.slots) as slot_sum
from cd.bookings as bkg
where bkg.starttime >= '2012-09-01' and bkg.starttime < '2012-10-01'
group by bkg.facid
order by slot_sum;

-- Sol
select facid, sum(slots) as "Total Slots"
	from cd.bookings
	where
		starttime >= '2012-09-01'
		and starttime < '2012-10-01'
	group by facid
order by sum(slots);