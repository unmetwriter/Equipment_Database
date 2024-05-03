SELECT bookings.BookingId,students.*,equipment.Name,bookings.NumberOfItems,bookings.StartDate,bookings.EndDate
FROM ((students INNER JOIN bookings USING(SocialSecurityNumber))  
INNER JOIN equipment USING (EquipmentId));


SELECT equipment.Item,types.Category,equipment.Description, TotalQuantity 
FROM equipment JOIN types 
ON equipment.TypeId = types.TypeId;

# Create a view of students, with concatenated name
CREATE VIEW student_view AS
SELECT SocialSecurityNumber, CONCAT(students.FirstName," ",students.LastName) as StudentName,Email,PhoneNumber
FROM Students;

drop view if exists bookings_view;
CREATE VIEW bookings_view AS 
SELECT BookingId,student_view.*,equipment.EquipmentId,equipment.Item,Quantity,StartDate,EndDate,ReturnDate
FROM student_view 
INNER JOIN 
bookings 
ON student_view.SocialSecurityNumber =bookings.SocialSecurityNumber
INNER JOIN 
equipment 
ON equipment.EquipmentId =bookings.EquipmentId;

# create a view of currently active bookings
drop view if exists active_bookings;
 CREATE VIEW active_bookings AS
 SELECT * FROM bookings_view 
 WHERE Enddate >=CURRENT_DATE() ;
SELECT ItemNumber FROM active_bookings;

# Create view that shows all available items (and the number of available items) from the equipment table
drop view if exists available_items;
CREATE VIEW available_items AS
SELECT equipment.Item, types.Category,equipment.Description, available_quantity(EquipmentId,TotalQuantity) as AvailableQuantity
FROM (equipment JOIN types ON equipment.TypeId = types.TypeId)
WHERE available_quantity(EquipmentId,TotalQuantity) >0;

SELECT * FROM available_items;

SELECT equipment.Item, types.Category,equipment.Description, available_quantity(EquipmentId,TotalQuantity) as AvailableQuantity
FROM (equipment JOIN types ON equipment.TypeId = types.TypeId)
WHERE available_quantity(EquipmentId,TotalQuantity) >0;




