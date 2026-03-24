-- My Sol
select bkg.facid, extract(month from bkg.starttime) as booking_month, sum(bkg.slots)
from cd.bookings as bkg
where extract(year from bkg.starttime) = '2012'
group by bkg.facid, booking_month
order by bkg.facid, booking_month;

-- Sol
select facid, extract(month from starttime) as month, sum(slots) as "Total Slots"
	from cd.bookings
	where extract(year from starttime) = 2012
	group by facid, month
order by facid, month;          