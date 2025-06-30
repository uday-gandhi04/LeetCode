# Write your MySQL query statement below
select d.name as Department, e.name as Employee, Salary 
from employee e join department d 
join (
    select max(salary)as s,departmentId
    from employee 
    group by departmentId
) b
on e.departmentid=d.id and b.s=salary and b.departmentId=d.id

