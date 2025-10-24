with q as (select person_id,person_name,weight,turn,
sum(weight) over (order by turn) as total_weight
from Queue)

select person_name 
from q
where total_weight<=1000
order by turn desc 
limit 1
