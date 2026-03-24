-- My Sol
select * 
from cd.facilities as fac
where upper(fac.name) like 'TENNIS%';

-- Sol
select * from cd.facilities where upper(name) like 'TENNIS%';          