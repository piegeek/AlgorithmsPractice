-- My Original Solution
select fac.name, date_trunc('month', bkg.starttime) as month,
extract(epoch from (sum(bkg.slots * interval '30 minutes')))
 / (extract(epoch from (date_trunc('month', bkg.starttime) + interval '1 month' - date_trunc('month', bkg.starttime))) * extract(epoch from('2012-01-01 20:30:00'::timestamp - '2012-01-01 08:00:00'::timestamp)))
 as utilization
from cd.bookings as bkg
inner join cd.facilities as fac on bkg.facid = fac.facid
group by fac.name, month
order by fac.name, month;

-- Gemini Solution
SELECT 
    fac.name, 
    date_trunc('month', bkg.starttime) AS month,
    ROUND(
        (extract(epoch from (SUM(bkg.slots * interval '30 minutes')))) / 
         extract(epoch from(
            EXTRACT(DAY FROM (date_trunc('month', bkg.starttime) + interval '1 month' - date_trunc('month', bkg.starttime))) 
            * interval '12.5 hours' 
         )
        ) * 100, 1
    ) AS utilization
FROM cd.bookings AS bkg
INNER JOIN cd.facilities AS fac ON bkg.facid = fac.facid
GROUP BY fac.name, month
ORDER BY fac.name, month;

-- My Sol with correction
select fac.name, date_trunc('month', bkg.starttime) as month,
round( (100.0 * extract(epoch from (sum(bkg.slots * interval '30 minutes')))
 / (extract(epoch from (date_trunc('month', bkg.starttime) + interval '1 month' - date_trunc('month', bkg.starttime))) * extract(epoch from('2012-01-01 20:30:00'::timestamp - '2012-01-01 08:00:00'::timestamp)) / extract(epoch from(interval '24 hours')))),
1 )as utilization
from cd.bookings as bkg
inner join cd.facilities as fac on bkg.facid = fac.facid
group by fac.name, month
order by fac.name, month;

-- Sol
select name, month, 
	round((100*slots)/
		cast(
			25*(cast((month + interval '1 month') as date)
			- cast (month as date)) as numeric),1) as utilisation
	from  (
		select facs.name as name, date_trunc('month', starttime) as month, sum(slots) as slots
			from cd.bookings bks
			inner join cd.facilities facs
				on bks.facid = facs.facid
			group by facs.facid, month
	) as inn
order by name, month    