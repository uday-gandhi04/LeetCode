# Write your MySQL query statement below
select round(sum(tiv_2016),2) as tiv_2016
from insurance a join( select tiv_2015, count(*) as tiv_count from insurance group by tiv_2015) b
join ( select lat,lon,count(*) as loc from insurance group by lat,lon) c
on a.tiv_2015=b.tiv_2015 and a.lat=c.lat and a.lon=c.lon
where b.tiv_count>1 and c.loc=1