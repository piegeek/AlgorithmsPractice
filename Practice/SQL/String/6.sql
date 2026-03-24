-- My Sol
select substr(mem.surname, 1, 1), count(*)
from cd.members as mem
group by substr(mem.surname, 1, 1)
order by substr(mem.surname, 1, 1);

-- Sol
select substr (mems.surname,1,1) as letter, count(*) as count 
    from cd.members mems
    group by letter
    order by letter