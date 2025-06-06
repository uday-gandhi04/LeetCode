# Write your MySQL query statement below

with a as (select distinct visited_on, sum(amount) over(order by visited_on range between interval 6 day preceding and current row) as amount, round(sum(amount) over(order by visited_on range between interval 6 day preceding and current row)/7,2) as average_amount
from customer)

select *
from  a
where visited_on > (select min(visited_on) from a) + interval 5 day