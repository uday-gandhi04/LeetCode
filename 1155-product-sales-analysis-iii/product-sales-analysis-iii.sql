select b.product_id, b.year as first_year, quantity,price
from sales join 
(select product_id,min(year) as year
from Sales
group by product_id) as b
on sales.product_id=b.product_id and sales.year=b.year