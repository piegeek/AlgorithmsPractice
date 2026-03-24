-- My Sol
select mem.firstname, mem.surname, round(sum(bkg.slots * 0.5), -1) as hours, rank() over (order by round(sum(bkg.slots * 0.5), -1) desc)
from cd.bookings as bkg
inner join cd.members as mem on bkg.memid = mem.memid
group by (mem.firstname, mem.surname)
order by rank, mem.surname, mem.firstname;

-- Sol "사실 일반적으로는 floor((x + 5) / 10) * 10 이라는 수식을 훨씬 많이 씁니다."
select firstname, surname,
	((sum(bks.slots)+10)/20)*10 as hours,
	rank() over (order by ((sum(bks.slots)+10)/20)*10 desc) as rank

	from cd.bookings bks
	inner join cd.members mems
		on bks.memid = mems.memid
	group by mems.memid
order by rank, surname, firstname; 