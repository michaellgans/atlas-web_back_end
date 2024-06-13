-- Task 6: Creates stored procedure to add new correction
DELIMITER $$

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_bonus INT
)
BEGIN
    -- Temporary project_id variable
    DECLARE project_id INT;

    INSERT INTO projects (name)
    VALUES (p_project_name)
    ON DUPLICATE KEY UPDATE id = LAST_INSERT_ID(id);
    
    SELECT LAST_INSERT_ID() INTO project_id;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, project_id, p_bonus);
END $$

DELIMITER ;
