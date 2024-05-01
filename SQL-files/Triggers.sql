DROP trigger if exists update_number_of_available_items;
DELIMITER // 
# Create a trigger  that updates the quantity of an available item  in the available items view.
create trigger update_number_of_available_items
after insert on bookings 
FOR EACH ROW
begin
UPDATE available_items 
SET available_items.AvailableQuantity = available_items.AvailableQuantity - new.NumberOfItems
WHERE EquipmentId = new.EquipmentId;
end; //

DROP trigger if exists stop_booking_insertion_if_already_exists;
#Create a trigger that will stop an insertion in the bookings table, if it already exists
DELIMITER //
create trigger stop_booking_insertion_if_already_exists before insert on bookings
FOR EACH ROW
begin
IF (exists(SELECT 1 FROM bookings WHERE (SocialSecurityNumber= new.SocialSecurityNumber AND EquipmentId = new.EquipmentId AND StartDate = new.StartDate AND EndDate =new.EndDate  ) )) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = "The booking already exists.";
END IF;
end;//
