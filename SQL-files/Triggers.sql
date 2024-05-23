
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



DROP trigger if exists stop_item_insert_if_already_exists;
DELIMITER //
create trigger stop_item_insert_if_already_exists before insert on equipment
FOR EACH ROW
begin
IF (exists(SELECT 1 FROM equipment WHERE (Item = new.Item))) THEN
	SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT ='Item already exists.';
END IF;
end;//
