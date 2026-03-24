-- My Sol
with facilities as (
	select fac.name, 
  	sum(
		case 
	  		when bkg.memid = 0 then bkg.slots * fac.guestcost
	  		else bkg.slots * fac.membercost
	  	end
	), 
  	ntile(3) over (order by sum(
		case 
	  		when bkg.memid = 0 then bkg.slots * fac.guestcost
	  		else bkg.slots * fac.membercost
	  	end
	) desc)
	from cd.bookings as bkg 
	inner join cd.facilities as fac on bkg.facid = fac.facid  
  	group by fac.name
)

select name,
case
	when ntile = 1 then 'high'
	when ntile = 2 then 'average'
	else 'low'
end as revenue
from facilities
order by ntile asc, name;

-- Sol
select name, case when class=1 then 'high'
		when class=2 then 'average'
		else 'low'
		end revenue
	from (
		select facs.name as name, ntile(3) over (order by sum(case
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			end) desc) as class
		from cd.bookings bks
		inner join cd.facilities facs
			on bks.facid = facs.facid
		group by facs.name
	) as subq
order by class, name; 