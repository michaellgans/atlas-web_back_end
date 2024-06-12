-- Task 4: Decreases the quantity of an item
-- when a new order comes in as a record
DELIMITER $$

CREATE TRIGGER decrease_inventory
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update items table.  NEW accesses new record
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END;
$$

DELIMITER ;
