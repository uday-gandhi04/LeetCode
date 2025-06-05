# Write your MySQL query statement below
select a.x,a.y,a.z, case when b.x is not null then 'Yes' else 'No' end as triangle
from triangle a left join (select x,y,z from triangle where x+y>z and x+z>y and y+z>x ) b
on a.x=b.x and a.y=b.y and a.z=b.z