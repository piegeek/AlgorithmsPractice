-- My Sol
select res.facid, res.tot_slots
from (
select bkg.facid, sum(bkg.slots) as tot_slots
from cd.bookings as bkg
group by bkg.facid
order by tot_slots desc
) as res
limit 1;

-- Sol: Use CTE's
with sum as (select facid, sum(slots) as totalslots
	from cd.bookings
	group by facid
)
select facid, totalslots 
	from sum
	where totalslots = (select max(totalslots) from sum);