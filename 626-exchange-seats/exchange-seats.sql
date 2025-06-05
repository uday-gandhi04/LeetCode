SELECT 
    a.id,
    COALESCE(b.student, a.student) AS student
FROM seat a
LEFT JOIN seat b 
    ON (a.id % 2 = 1 AND b.id = a.id + 1)
    OR (a.id % 2 = 0 AND b.id = a.id - 1)
ORDER BY a.id;
