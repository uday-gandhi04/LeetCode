# Write your MySQL query statement below
with a as (select employee.id,employee.name as Employee, salary as Salary, department.name as Department  from employee join department on employee.departmentid=department.id)

select Department, employee, salary 
from a join (select id,
dense_rank() over (partition by department order by salary desc ) as s
from a) b 
on a.id=b.id
where b.s<4