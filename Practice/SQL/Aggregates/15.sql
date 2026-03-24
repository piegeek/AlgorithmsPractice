-- My Sol - Learn about window functions (count() over)
select count(*) over (), 
case
	when mem.memid = 0 then 'GUEST'
	else mem.firstname
end as firstname,
case
	when mem.memid = 0 then 'GUEST'
	else mem.surname
end as surname
from cd.members as mem
group by mem.memid
order by mem.joindate;

-- Sol
select (select count(*) from cd.members) as count, firstname, surname
	from cd.members
order by joindate