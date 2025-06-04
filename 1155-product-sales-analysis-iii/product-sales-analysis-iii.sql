# Write your MySQL query statement below
select a.product_id,year as first_year,quantity,price
from sales a join (select product_id,min(year) as fy from sales group by product_id) as b
on a.product_id=b.product_id 
where a.year=b.fy