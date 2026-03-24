-- My Sol
select mem.recommendedby, count(*)
from cd.members as mem
where mem.recommendedby > 0
group by mem.recommendedby
order by mem.recommendedby;

-- Sol
select recommendedby, count(*) 
	from cd.members
	where recommendedby is not null
	group by recommendedby
order by recommendedby;          