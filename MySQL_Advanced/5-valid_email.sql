-- Task 5: resets valid_email when email has changed
DELIMITER $$

CREATE TRIGGER update_email
-- Check before updating
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;
$$

DELIMITER ;
