-- My Sol; Self join
SELECT DISTINCT mem1.firstname, mem1.surname
FROM 
CD.MEMBERS AS mem1
INNER JOIN CD.MEMBERS AS mem2 ON mem1.memid = mem2.recommendedby
ORDER BY mem1.surname, mem1.firstname;

-- Remember order by multiple: use commas

-- Sol
select distinct recs.firstname as firstname, recs.surname as surname
	from 
		cd.members mems
		inner join cd.members recs
			on recs.memid = mems.recommendedby
order by surname, firstname;       