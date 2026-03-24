-- My Sol
select date_trunc('month', bkg.starttime) as month,
count(*)
from cd.bookings as bkg
group by month
order by month;

-- Sol
select date_trunc('month', starttime) as month, count(*)
	from cd.bookings
	group by month
	order by month   