# Write your MySQL query statement below
select max(b.num) as num
from Mynumbers a join (select num from Mynumbers group by num having count(*)=1) as b
on a.num=b.num