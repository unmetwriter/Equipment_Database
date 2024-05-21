
# Create a procedure which returns all items in a certain category
drop procedure if exists items_in_category;
DELIMITER //
create procedure items_in_category(type_id int)
begin 
SELECT equipment.Item,types.Category,equipment.Description, available_quantity(EquipmentId,equipment.TotalQuantity) as AvailableQuantity
FROM equipment JOIN types 
ON equipment.TypeId = types.TypeId
WHERE equipment.TypeId = type_id;
end; //
