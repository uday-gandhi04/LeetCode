select c.product_id, (case when a.new_price is null then 10 else a.new_price end) as price 
from 
products a join 
    (select product_id,max(change_date) as latest_date 
    from products 
    where change_date<='2019-08-16' 
    group by product_id) b 
        right join (select distinct product_id from products) c
on a.product_id=b.product_id and a.change_date=b.latest_date and a.product_id=c.product_id