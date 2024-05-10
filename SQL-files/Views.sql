SELECT bookings.BookingId,students.*,equipment.Name,bookings.NumberOfItems,bookings.StartDate,bookings.EndDate
FROM ((students INNER JOIN bookings USING(SocialSecurityNumber))  
INNER JOIN equipment USING (EquipmentId));


SELECT equipment.Item,types.Category,equipment.Description, TotalQuantity 
FROM equipment JOIN types 
ON equipment.TypeId = types.TypeId;




drop view if exists bookings_view;
CREATE VIEW bookings_view AS 
SELECT BookingId,students.*,equipment.EquipmentId,equipment.Item,Quantity,StartDate,EndDate,ReturnDate
FROM student_view 
INNER JOIN 
bookings 
ON students.SocialSecurityNumber =bookings.SocialSecurityNumber
INNER JOIN 
equipment 
ON equipment.EquipmentId =bookings.EquipmentId;

SELECT * FROM bookings;

# create a view of currently active bookings
drop view if exists active_bookings;
 CREATE VIEW active_bookings AS
 SELECT * FROM bookings_view 
 WHERE Enddate >=CURRENT_DATE();
SELECT * FROM active_bookings;

SELECT * FROM active_bookings;
# Create view that shows all available items (and the number of available items) from the equipment table
drop view if exists available_items;
CREATE VIEW available_items AS
SELECT equipment.EquipmentId,equipment.Item, types.Category,equipment.Description, available_quantity(EquipmentId,TotalQuantity) as AvailableQuantity
FROM (equipment JOIN types ON equipment.TypeId = types.TypeId)
WHERE available_quantity(EquipmentId,TotalQuantity) >0;

SELECT * FROM available_items;

SELECT equipment.Item, types.Category,equipment.Description, available_quantity(EquipmentId,TotalQuantity) as AvailableQuantity
FROM (equipment JOIN types ON equipment.TypeId = types.TypeId)
WHERE available_quantity(EquipmentId,TotalQuantity) >0;





