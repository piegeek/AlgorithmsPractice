-- My Sol
select generate_series('2012-10-01'::timestamp, '2012-10-31'::timestamp, interval '1 day') as ts;

-- Sol
select generate_series(timestamp '2012-10-01', timestamp '2012-10-31', interval '1 day') as ts;  