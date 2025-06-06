# Write your MySQL query statement below
select sell_date,count(distinct product) as num_sold, GROUP_CONCAT(distinct product ORDER BY product SEPARATOR ',') as products
from activities
group by sell_date