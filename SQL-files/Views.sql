SELECT bookings.BookingId,students.*,equipment.Name,bookings.NumberOfItems,bookings.StartDate,bookings.EndDate
FROM ((students INNER JOIN bookings USING(SocialSecurityNumber))  
INNER JOIN equipment USING (EquipmentId));


SELECT equipment.Name as Item,types.Name as Category,equipment.Description, TotalNumberItems 
FROM equipment JOIN types 
ON equipment.TypeId = types.TypeId;

# Create a view of students, with concatenated name
CREATE VIEW student_view AS
SELECT SocialSecurityNumber, CONCAT(students.FirstName," ",students.LastName) as StudentName,Email,PhoneNumber
FROM Students;

CREATE VIEW bookings_view AS 
SELECT BookingId,student_view.*,equipment.EquipmentId as ItemNumber,equipment.Name as Item,NumberOfItems,StartDate,EndDate
FROM student_view 
INNER JOIN 
bookings 
ON student_view.SocialSecurityNumber =bookings.SocialSecurityNumber
INNER JOIN 
equipment 
ON equipment.EquipmentId =bookings.EquipmentId;

DROP VIEW bookings_view;
SELECT * FROM bookings_view;

# create a view of currently active bookings
 CREATE VIEW active_bookings AS
 SELECT * FROM bookings_view 
 WHERE Enddate >=CURRENT_DATE();

# Create view that shows all available items (and the number of available items) from the equipment table
CREATE VIEW available_items AS
SELECT equipment.Name as Item, types.Name as Category,equipment.Description, available_quantity(EquipmentId,TotalNumberItems) as AvailableQuantity
FROM (equipment JOIN types ON equipment.TypeId = types.TypeId)
WHERE available_quantity(EquipmentId,TotalNumberItems) >0;
SELECT * FROM available_items;
DROP VIEW available_items;





