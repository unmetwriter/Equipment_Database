
# Create a procedure which returns all items in a certain category
drop procedure if exists items_in_category;
DELIMITER //
create procedure items_in_category(type_id varchar(50))
begin 
SELECT equipment.Item,types.Category,equipment.Description, available_quantity(EquipmentId,equipment.TotalQuantity) as " Available Quantity"
FROM equipment JOIN types 
ON equipment.TypeId = types.TypeId
WHERE equipment.TypeId = type_id;
end; //
Call items_in_category(2);