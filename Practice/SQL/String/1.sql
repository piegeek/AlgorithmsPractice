-- My Sol
select mem.surname || ', ' || mem.firstname as name
from cd.members as mem;

-- Sol
select surname || ', ' || firstname as name from cd.members 