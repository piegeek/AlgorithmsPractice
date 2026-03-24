-- My Sol
select bkg.starttime, bkg.endtime
from (
	select starttime as starttime, 
  	starttime + interval '1 hour' * slots * 0.5 as endtime
  	from cd.bookings
  	order by (starttime + interval '1 hour' * slots * 0.5, starttime) desc
	limit 10
) as bkg;

-- Sol
select starttime, starttime + slots*(interval '30 minutes') endtime
	from cd.bookings
	order by endtime desc, starttime desc
	limit 10          