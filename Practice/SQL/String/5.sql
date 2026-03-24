-- My Sol
select lpad(zipcode::varchar, 5, '0') as zip
from cd.members
order by lpad(zipcode::varchar, 5, '0');

-- Sol
select lpad(cast(zipcode as char(5)),5,'0') zip from cd.members order by zip 