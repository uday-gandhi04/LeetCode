# Write your MySQL query statement below
select distinct product_name, total as unit
from orders o join 
(select product_id,sum(unit) as total from orders where month(order_date) =2 and year(order_date)=2020 group by product_id) b join products 
on o.product_id =b.product_id and o.product_id=products.product_id
where b.total>=100
