# Write your MySQL query statement below
select b.id
from Weather as a join Weather as b 
on b.recordDate=a.recordDate + INTERVAL 1 DAY 
where a.temperature<b.temperature