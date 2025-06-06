# Write your MySQL query statement below
delete a from person a left join (select min(id) as id ,email from person group by email) b
on a.id=b.id
where b.id is null
