-- Task 6: Creates stored procedure to add new correction
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_bonus INT
)
BEGIN
    -- Temporary project_id variable
    DECLARE check_project_id INT;

    -- Does the project exist?
    SELECT id 
    INTO check_project_id 
    FROM projects 
    WHERE name = p_project_name;

    IF check_project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (p_project_name);
        SET check_project_id = LAST_INSERT_ID();
    END IF;

INSERT INTO corrections (user_id, project_id, score)
VALUES (p_user_id, check_project_id, p_bonus);
END $$

DELIMITER ;
