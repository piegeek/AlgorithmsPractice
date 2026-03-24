-- My Sol
select (extract(epoch from '2012-09-02 00:00:00'::timestamp) - extract(epoch from '2012-08-31 01:00:00'::timestamp))::int as date_part;

-- Sol
select extract(epoch from (timestamp '2012-09-02 00:00:00' - '2012-08-31 01:00:00')); 

-- 컴퓨팅 세계에서 **에포크(Epoch)**는 시간의 흐름을 측정하기 위한 **'기준점(00:00:00)'**을 의미합니다.
