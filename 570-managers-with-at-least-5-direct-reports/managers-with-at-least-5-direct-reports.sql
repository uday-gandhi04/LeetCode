# Write your MySQL query statement below
select a.NAME
from employee as a join employee as b
on a.id=b.managerid
group by b.managerID
having count(*) >=5