
drop view if exists bookings_view;
CREATE VIEW bookings_view AS 
SELECT BookingId,students.*,equipment.EquipmentId,equipment.Item,Quantity,StartDate,EndDate,ReturnDate
FROM studentss
INNER JOIN 
bookings 
ON students.SocialSecurityNumber =bookings.SocialSecurityNumber
INNER JOIN 
equipment ON equipment.EquipmentId =bookings.EquipmentId;


# create a view of currently active bookings
drop view if exists active_bookings;
 CREATE VIEW active_bookings AS
 SELECT * FROM bookings_view 
 WHERE Enddate >=CURRENT_DATE() AND ReturnDate IS NULL;


# Create view that shows all available items (and the number of available items) from the equipment table
drop view if exists available_items;
CREATE VIEW available_items AS
SELECT equipment.EquipmentId,equipment.Item, types.Category,equipment.Description, available_quantity(EquipmentId,TotalQuantity) as AvailableQuantity
FROM (equipment JOIN types ON equipment.TypeId = types.TypeId)
WHERE available_quantity(EquipmentId,TotalQuantity) >0;


drop view if exists booked_items;
CREATE VIEW booked_items AS
SELECT equipment.EquipmentId,equipment.Item, types.Category, equipment.Description,SUM(active_bookings.Quantity) as BookedQuantity
FROM ((equipment INNER JOIN types USING(TypeId)) INNER JOIN active_bookings USING(EquipmentId))
GROUP BY active_bookings.equipmentId;



