-- My Sol
select count(distinct mem.memid)
from cd.bookings as bkg
inner join cd.members as mem on bkg.memid = mem.memid;

-- Sol 1
select count(distinct memid) from cd.bookings          

-- Sol 2 (subqueries)
select count(*) from 
	(select distinct memid from cd.bookings) as mems