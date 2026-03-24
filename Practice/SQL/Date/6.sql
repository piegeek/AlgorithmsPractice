-- My Sol 1. Union all extract month from timestamp and intervals

-- My Sol 2. Remark; If we have to do (i, i+1) use interval!!
select extract(month from cal) as month,
(cal + interval '1 month') - cal as length
from (
	select generate_series('2012-01-01'::timestamp, '2012-12-01'::timestamp, interval '1 month') as cal  
)
order by month;

-- Sol
select 	extract(month from cal.month) as month,
	(cal.month + interval '1 month') - cal.month as length
	from
	(
		select generate_series(timestamp '2012-01-01', timestamp '2012-12-01', interval '1 month') as month
	) cal
order by month;  