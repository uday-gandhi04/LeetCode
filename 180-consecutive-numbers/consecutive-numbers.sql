select distinct a.num as ConsecutiveNums
from Logs a join Logs b join logs c
on a.num=b.num and b.num=c.num and a.id=b.id-1 and b.id=c.id-1