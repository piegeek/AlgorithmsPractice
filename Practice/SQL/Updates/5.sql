-- My Sol
update cd.facilities
set membercost = 6, guestcost = 30
where name like 'Tennis Court%';

-- Sol
update cd.facilities
    set
        membercost = 6,
        guestcost = 30
    where facid in (0,1);    