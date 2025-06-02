# Write your MySQL query statement below
select contest_id, round((count(contest_id)/(select count(distinct user_id)from  users))*100,2) as percentage
from users join register
on users.user_id=register.user_id
group by contest_id 
order by percentage desc, contest_id asc