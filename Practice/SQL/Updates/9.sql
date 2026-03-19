-- My Sol
delete from cd.members
where memid not in (
	  select memid 
	  from cd.bookings
);

-- Remark: Be aware of subqueries that do the same thing

-- Sol
delete from cd.members where memid not in (select memid from cd.bookings);         