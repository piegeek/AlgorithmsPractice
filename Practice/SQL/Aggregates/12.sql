-- My Sol
select bkg.facid, extract(month from bkg.starttime) as booking_month, sum(bkg.slots)
from cd.bookings as bkg
where extract(year from bkg.starttime) = '2012'
group by rollup (bkg.facid, booking_month)
order by bkg.facid, extract(month from bkg.starttime);

-- Sol (Using CTE's)
with bookings as (
	select facid, extract(month from starttime) as month, slots
	from cd.bookings
	where
		starttime >= '2012-01-01'
		and starttime < '2013-01-01'
)
select facid, month, sum(slots) from bookings group by facid, month
union all
select facid, null, sum(slots) from bookings group by facid
union all
select null, null, sum(slots) from bookings
order by facid, month;