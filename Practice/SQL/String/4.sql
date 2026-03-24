-- My Sol
select mem.memid, mem.telephone
from cd.members as mem
where mem.telephone like '(___) %'
order by mem.memid;

-- Sol; Remark: Use regexes
select memid, telephone from cd.members where telephone ~ '[()]'; 