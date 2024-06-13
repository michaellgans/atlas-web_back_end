-- Task 11: Creates a new view to show all students
-- that have a score under 80

DROP VIEW IF EXISTS need_meeting;

CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 AND last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 30 DAY);
