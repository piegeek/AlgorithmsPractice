-- Note: "Aggregate functions are not allowed in WHERE" -> Use "HAVING" instead

-- My Sol
select facid, tot_slots
from
(
select bkg.facid, sum(bkg.slots) as tot_slots
from cd.bookings as bkg
group by bkg.facid
order by bkg.facid
)
where tot_slots > 1000;

-- Sol
select facid, sum(slots) as "Total Slots"
        from cd.bookings
        group by facid
        having sum(slots) > 1000
        order by facid          