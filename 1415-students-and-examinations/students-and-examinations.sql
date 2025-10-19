select 
    s.student_id,s.student_name,sn.subject_name,count(e.subject_name) as attended_exams
from 
    (students s join subjects sn) left join Examinations e
on s.student_id =e.student_id and sn.subject_name=e.subject_name
group by s.student_id,sn.subject_name
order by s.student_id,sn.subject_name