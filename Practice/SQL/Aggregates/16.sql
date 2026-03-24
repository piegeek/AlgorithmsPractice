-- My Sol - Learn about window functions(row_number() over)
select row_number() over (), firstname, surname
from cd.members
order by joindate

-- Sol
select row_number() over(order by joindate), firstname, surname
	from cd.members
order by joindate     