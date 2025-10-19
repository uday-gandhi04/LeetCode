select name from employee
where id in (select managerId
from Employee
group by managerId
having Count(*)>=5)