select b.id
from weather a left join weather b
on a.recordDate+interval 1 day = b.recordDate
where a.temperature < b.temperature