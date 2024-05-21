DROP function if exists available_quantity;
DELIMITER %% 
CREATE FUNCTION available_quantity(equipment_id INT,number_of_items INT )
RETURNS INT DETERMINISTIC
BEGIN
DECLARE result INT;
DECLARE booked_quantity INT;
SET result = number_of_items;

IF (equipment_id NOT IN(SELECT EquipmentId FROM active_bookings)) THEN 
    SET booked_quantity =0;
ELSE
    SET booked_quantity = (SELECT SUM(Quantity) FROM active_bookings GROUP BY EquipmentId  HAVING EquipmentId = equipment_id);
END IF;
SET result = result -booked_quantity;
RETURN result;
END; %%


