# Write your MySQL query statement below

select x.student_id as student_id, x.subject as subject, first_score, latest_score

from 
((select s.student_id as student_id, s.subject as subject ,score as first_score
from scores s join 
    (select student_id,subject
    from Scores
    group by student_id,subject
    having count(*)>1) b
on s.student_id=b.student_id and s.subject=b.subject
group by s.student_id,s.subject) 
) x
join(
select  s.student_id as student_id, s.subject as subject ,score as latest_score from 
(select s.student_id as student_id, s.subject as subject ,max(exam_date) as datee
from scores s join 
    (select student_id,subject
    from Scores
    group by student_id,subject
    having count(*)>1) b
on s.student_id=b.student_id and s.subject=b.subject
group by s.student_id,s.subject) a
join scores s 
where a.student_id =s.student_id and a.subject=s.subject and a.datee=s.exam_date
) y
on x.student_id=y.student_id and x.subject=y.subject

where latest_score>first_score
order by x.student_id,x.subject

