-- My Sol
SELECT mem.firstname AS memfname, 
mem.surname AS memsname, 
rec.firstname AS recfname,
rec.surname AS recsname
FROM
CD.MEMBERS as mem
LEFT JOIN CD.MEMBERS as rec ON mem.recommendedby = rec.memid
ORDER BY mem.surname, mem.firstname;

-- Remember: Left join - get all members of left table even if they're not matched