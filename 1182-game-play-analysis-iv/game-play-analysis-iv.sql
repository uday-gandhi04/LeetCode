# Write your MySQL query statement below
select 
round( 
    (select count(distinct a.player_id) from activity as a 
        join (select player_id,min(event_date) as event_date
            from activity
            group by player_id ) as b
    on a.player_id=b.player_id and a.event_date=b.event_Date + interval 1 day)
/(select count(distinct player_id) from activity),2) as fraction
