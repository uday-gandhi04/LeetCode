# Write your MySQL query statement below
select 
    name , bonus
from
    Employee left join bonus
on
    employee.empid=bonus.empid
where 
    bonus <1000 or bonus is null
