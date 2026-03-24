-- My Sol - Use subqueries
with bookings as (
	select fac.facid, sum(bkg.slots) as total
	from cd.facilities as fac
  	inner join cd.bookings as bkg on fac.facid = bkg.facid
  	group by fac.facid
)

select facid, total
from bookings
where total = 
(
	select max(total)
	from bookings  
)