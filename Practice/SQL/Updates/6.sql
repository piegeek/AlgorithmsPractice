-- My Sol
update cd.facilities
set guestcost = 1.1 * (select guestcost from cd.facilities where name = 'Tennis Court 1'),
membercost = 1.1 * (select membercost from cd.facilities where name = 'Tennis Court 1')
where name = 'Tennis Court 2';

-- Sol
update cd.facilities facs
    set
        membercost = (select membercost * 1.1 from cd.facilities where facid = 0),
        guestcost = (select guestcost * 1.1 from cd.facilities where facid = 0)
    where facs.facid = 1;          