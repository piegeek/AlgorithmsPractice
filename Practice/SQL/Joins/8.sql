-- My Sol
select mem.firstname || ' ' || mem.surname as member,
fac.name as facility,
case 
	when mem.memid = 0 then bkg.slots * fac.guestcost
	else bkg.slots * fac.membercost
end as cost
from
cd.members as mem
inner join cd.bookings as bkg on mem.memid = bkg.memid
inner join cd.facilities as fac on fac.facid = bkg.facid
where bkg.starttime >= '2012-09-14' and bkg.starttime < '2012-09-15' and (
  mem.memid = 0 and bkg.slots * fac.guestcost > 30
  or 
  mem.memid > 0 and bkg.slots * fac.membercost > 30
)
order by cost desc;

-- Remark: Can do like this select member, facility, cost from ( select ... as member, ... as facility, ... as cost from table1 join table2 join table3 where ... ) where ...

-- Sol
select member, facility, cost from (
	select 
		mems.firstname || ' ' || mems.surname as member,
		facs.name as facility,
		case
			when mems.memid = 0 then
				bks.slots*facs.guestcost
			else
				bks.slots*facs.membercost
		end as cost
		from
			cd.members mems
			inner join cd.bookings bks
				on mems.memid = bks.memid
			inner join cd.facilities facs
				on bks.facid = facs.facid
		where
			bks.starttime >= '2012-09-14' and
			bks.starttime < '2012-09-15'
	) as bookings
	where cost > 30
order by cost desc;    