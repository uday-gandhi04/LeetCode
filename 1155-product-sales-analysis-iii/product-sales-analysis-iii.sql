select sales.product_id,fs.year as first_year, quantity,price
from sales join 
(select product_id,min(year) as year
from sales
group by product_id) as fs
on sales.product_id =fs.product_id and sales.year=fs.year