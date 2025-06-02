# Write your MySQL query statement below
select round(sum(delivery.order_date=firstOrder.fo and delivery.order_date= customer_pref_delivery_date)*100/count(distinct delivery.customer_id),2) as immediate_percentage
from delivery join (select customer_id, min(order_date) as fo from delivery group by customer_id) as firstOrder
on delivery.customer_id=firstOrder.customer_id 