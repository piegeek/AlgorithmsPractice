-- My Sol
select distinct
mem.firstname || ' ' || mem.surname as member,
case
	when mem.recommendedby = NULL then NULL
	else rec.firstname || ' ' || rec.surname
end as recommender
from cd.members as mem
left join cd.members as rec on mem.recommendedby = rec.memid
order by mem.firstname || ' ' || mem.surname

-- Remark: subqueries can come in select clause, and where clause (aggregates)
-- Subqueries are commonly used with aggregates
-- In this problem it is a correlated subquery (emulate outer join, in select clause)
-- Like two for-loops

-- Sol
select distinct mems.firstname || ' ' ||  mems.surname as member,
	(select recs.firstname || ' ' || recs.surname as recommender 
		from cd.members recs 
		where recs.memid = mems.recommendedby
	)
	from 
		cd.members mems
order by member;       