-- My Sol
-- [Original formula I formulated]
-- initialoutlay + n * monthlymaintenance = rev + n * membercost
-- (intialoutlay - rev) / (membercost - monthlymaintenance)

-- [This is the formula]
-- initialoutlay + n * monthlymaintenance = n * (rev / 3)
-- initialoutlay / (rev / 3 - monthlymaintenance)

with curr_revenues as (
	select fac.name, sum(
		case 
	  		when bkg.memid = 0 then bkg.slots * fac.guestcost
	  		else bkg.slots * fac.membercost
	 	end
	) as rev
	from cd.bookings as bkg
	inner join cd.facilities as fac on bkg.facid = fac.facid 
  	group by fac.name
)	

select fac.name, fac.initialoutlay / (curr_revs.rev / 3 - fac.monthlymaintenance) as months
from cd.facilities as fac
inner join curr_revenues as curr_revs on fac.name = curr_revs.name
order by fac.name;

-- Sol
select 	facs.name as name,
	facs.initialoutlay/((sum(case
			when memid = 0 then slots * facs.guestcost
			else slots * membercost
		end)/3) - facs.monthlymaintenance) as months
	from cd.bookings bks
	inner join cd.facilities facs
		on bks.facid = facs.facid
	group by facs.facid
order by name; 