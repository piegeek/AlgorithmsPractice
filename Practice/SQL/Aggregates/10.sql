-- My Sol 1 - Using "HAVING" this doesn't work for column name aliases
select fac.name, sum(
  	case 
  		when bkg.memid = 0 then bkg.slots * fac.guestcost
  		else bkg.slots * fac.membercost
  	end
) as revenue
from cd.bookings as bkg
inner join cd.facilities as fac on fac.facid = bkg.facid
group by fac.name
having sum(
  	case 
  		when bkg.memid = 0 then bkg.slots * fac.guestcost
  		else bkg.slots * fac.membercost
  	end
) < 1000
order by revenue;

-- My Sol 2 - Subquery
select res.name, res.revenue
from (
  	select fac.name, sum(
	  	case
	  		when bkg.memid = 0 then bkg.slots * fac.guestcost
	  		else bkg.slots * fac.membercost
	  	end
	  ) as revenue
  	from cd.bookings as bkg
  	inner join cd.facilities as fac on bkg.facid = fac.facid
  	group by fac.name
  
  ) as res
where res.revenue < 1000
order by res.revenue;

-- Sol
select name, revenue from (
	select facs.name, sum(case 
				when memid = 0 then slots * facs.guestcost
				else slots * membercost
			end) as revenue
		from cd.bookings bks
		inner join cd.facilities facs
			on bks.facid = facs.facid
		group by facs.name
	) as agg where revenue < 1000
order by revenue;          

-- Postgres, unlike some other RDBMSs like SQL Server and MySQL, 
-- doesn't support putting column names in the HAVING clause. 
-- This means that for this query to work, you'd have to produce something like below:
select facs.name, sum(case 
		when memid = 0 then slots * facs.guestcost
		else slots * membercost
	end) as revenue
	from cd.bookings bks
	inner join cd.facilities facs
		on bks.facid = facs.facid
	group by facs.name
	having sum(case 
		when memid = 0 then slots * facs.guestcost
		else slots * membercost
	end) < 1000
order by revenue;

-- In general, I recommend using HAVING for simple queries, as it increases clarity. 
-- Otherwise, this subquery approach is often easier to use.