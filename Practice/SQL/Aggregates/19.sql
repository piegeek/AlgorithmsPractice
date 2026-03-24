-- My Sol
with revenues as (
	select fac.name, sum(
	  case
	  	when bkg.memid = 0 then bkg.slots * fac.guestcost
	  	else bkg.slots * fac.membercost
	  end
	)
  	from cd.bookings as bkg
  	inner join cd.facilities as fac on bkg.facid = fac.facid
  	group by fac.name
)

select name, rank() over (order by sum desc)
from revenues
limit 3;

-- Sol
select name, rank from (
	select facs.name as name, rank() over (order by sum(case
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			end) desc) as rank
		from cd.bookings bks
		inner join cd.facilities facs
			on bks.facid = facs.facid
		group by facs.name
	) as subq
	where rank <= 3
order by rank;  