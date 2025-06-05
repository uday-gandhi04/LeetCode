# Write your MySQL query statement below
(select name as results
from users a join (select distinct user_id ,count(*) as cnt
from movieRating 
group by user_id) b
on a.user_id=b.user_id
order by cnt desc, name  limit 1)

union all

(select title as results
from Movies m join (select distinct movie_id, avg(rating) as avgrating 
from movierating where created_at between '2020-02-01' and '2020-02-29'
group by movie_id ) r
on m.movie_id=r.movie_id
order by avgrating desc, title asc limit 1)