-- My Sol
select ('2012-03-01 01:00:00'::timestamp) - '2012-02-11 01:00:00'::timestamp as remaining;

-- Sol
select (date_trunc('month',ts.testts) + interval '1 month') 
		- date_trunc('day', ts.testts) as remaining
	from (select timestamp '2012-02-11 01:00:00' as testts) ts     