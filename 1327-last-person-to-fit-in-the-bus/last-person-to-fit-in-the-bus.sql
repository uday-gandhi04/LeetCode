# Write your MySQL query statement below
select person_name 
from queue a join (select person_id,sum(weight) over(order by turn) as totalweight from queue) b
on a.person_id = b.person_id 
where b.totalweight <=1000
order by totalweight desc limit 1

