select round(count(p.player_id)/count(distinct activity.player_id),2) as fraction
from activity left join 
    (select player_id, min(event_date) as event_date
    from activity
    group by player_id) as p
on activity.player_id = p.player_id and activity.event_date-interval 1 day=p.event_date
