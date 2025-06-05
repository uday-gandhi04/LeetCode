# Write your MySQL query statement below
select distinct a.employee_id,a.name, count(*) as reports_count,round(avg(b.age),0) as average_age
from employees a join employees b
on a.employee_id=b.reports_to
group by employee_id
order by employee_id