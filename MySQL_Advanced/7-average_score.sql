-- Task 7: Creates stored procedure to calculate average
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN p_user_id INT
)
BEGIN
    -- Temporary variable
    DECLARE new_average_grade DECIMAL(10, 2);

    -- Calculate the grade
    SELECT AVG(score) INTO new_average_grade
    FROM corrections
    WHERE user_id = p_user_id;

    -- Update existing average
    UPDATE users
    SET average_score = new_average_grade
    WHERE id = p_user_id;
END;
$$

DELIMITER ;
