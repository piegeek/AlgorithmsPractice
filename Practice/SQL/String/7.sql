-- My Sol
select mem.memid, translate(mem.telephone, '-() ', '')
from cd.members as mem
order by mem.memid;

-- Sol
select memid, translate(telephone, '-() ', '') as telephone
    from cd.members
    order by memid;  