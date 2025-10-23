select round(sum(case when d.order_date=d.customer_pref_delivery_date then 1 else 0 end)*100/count(*),2) as immediate_percentage

from delivery d join (select customer_id,min(order_date) as order_date from delivery group by customer_id) as i
on (d.customer_id,d.order_date)=(i.customer_id,i.order_date)
