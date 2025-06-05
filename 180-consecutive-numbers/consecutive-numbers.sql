# Write your MySQL query statement below
select distinct a.num as ConsecutiveNums
from logs a join logs b join logs c
on a.id=b.id-1 and a.id=c.id-2
where a.num=b.num and a.num=c.num