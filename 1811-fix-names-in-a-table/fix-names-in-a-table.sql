# Write your MySQL query statement below
select user_id,concat(Upper(left(name,1)),lower(right(name,LENGTH(name)-1))) as name
from users
order by user_id