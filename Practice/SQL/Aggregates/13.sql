-- My Sol - No floating point formatting
select bkg.facid, fac.name, sum(bkg.slots * 0.5) as tot_hours
from cd.bookings as bkg
inner join cd.facilities as fac on bkg.facid = fac.facid
group by bkg.facid, fac.name
order by bkg.facid;

-- Sol
select facs.facid, facs.name,
	trim(to_char(sum(bks.slots)/2.0, '9999999999999999D99')) as "Total Hours"

	from cd.bookings bks
	inner join cd.facilities facs
		on facs.facid = bks.facid
	group by facs.facid, facs.name
order by facs.facid;  