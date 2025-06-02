# Write your MySQL query statement below
select project_id, round(sum(e.experience_years)/count(*),2) as average_years
from project as p join employee as e
on p.employee_id=e.employee_id
group by p.project_id