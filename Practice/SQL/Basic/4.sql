-- Both below work
-- Sol 1
SELECT facid, name, membercost, monthlymaintenance FROM CD.FACILITIES
WHERE membercost > 0 and membercost < monthlymaintenance / 50

-- Sol 2 (in sql integer division gets rounded)
SELECT facid, name, membercost, monthlymaintenance FROM CD.FACILITIES
WHERE membercost > 0 and membercost < monthlymaintenance * (1.0/50)