# Write your MySQL query statement below
select s.user_id, round(ifnull(sum(action="confirmed")/count(c.user_id),0),2) as confirmation_rate
from signups as s left join confirmations as c
on s.user_id=c.user_id
group by s.user_id 