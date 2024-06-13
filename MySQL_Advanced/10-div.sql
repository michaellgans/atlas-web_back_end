-- Task 10: Divides two numbers
DROP FUNCTION IF EXISTS SafeDiv;

DELIMITER $$
CREATE FUNCTION SafeDiv(a FLOAT, b FLOAT)
RETURNS FLOAT
BEGIN
    DECLARE result FLOAT;

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END $$

DELIMITER ;
