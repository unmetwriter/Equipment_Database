-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: dv1663
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `bookings_view`
--

DROP TABLE IF EXISTS `bookings_view`;
/*!50001 DROP VIEW IF EXISTS `bookings_view`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `bookings_view` AS SELECT 
 1 AS `BookingId`,
 1 AS `SocialSecurityNumber`,
 1 AS `FirstName`,
 1 AS `LastName`,
 1 AS `Email`,
 1 AS `PhoneNumber`,
 1 AS `EquipmentId`,
 1 AS `Item`,
 1 AS `Quantity`,
 1 AS `StartDate`,
 1 AS `EndDate`,
 1 AS `ReturnDate`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `available_items`
--

DROP TABLE IF EXISTS `available_items`;
/*!50001 DROP VIEW IF EXISTS `available_items`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `available_items` AS SELECT 
 1 AS `EquipmentId`,
 1 AS `Item`,
 1 AS `Category`,
 1 AS `Description`,
 1 AS `AvailableQuantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `booked_items`
--

DROP TABLE IF EXISTS `booked_items`;
/*!50001 DROP VIEW IF EXISTS `booked_items`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `booked_items` AS SELECT 
 1 AS `EquipmentId`,
 1 AS `Item`,
 1 AS `Category`,
 1 AS `Description`,
 1 AS `BookedQuantity`*/;
SET character_set_client = @saved_cs_client;

--
-- Temporary view structure for view `active_bookings`
--

DROP TABLE IF EXISTS `active_bookings`;
/*!50001 DROP VIEW IF EXISTS `active_bookings`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `active_bookings` AS SELECT 
 1 AS `BookingId`,
 1 AS `SocialSecurityNumber`,
 1 AS `FirstName`,
 1 AS `LastName`,
 1 AS `Email`,
 1 AS `PhoneNumber`,
 1 AS `EquipmentId`,
 1 AS `Item`,
 1 AS `Quantity`,
 1 AS `StartDate`,
 1 AS `EndDate`,
 1 AS `ReturnDate`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `bookings_view`
--

/*!50001 DROP VIEW IF EXISTS `bookings_view`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `bookings_view` AS select `bookings`.`BookingId` AS `BookingId`,`students`.`SocialSecurityNumber` AS `SocialSecurityNumber`,`students`.`FirstName` AS `FirstName`,`students`.`LastName` AS `LastName`,`students`.`Email` AS `Email`,`students`.`PhoneNumber` AS `PhoneNumber`,`equipment`.`EquipmentId` AS `EquipmentId`,`equipment`.`Item` AS `Item`,`bookings`.`Quantity` AS `Quantity`,`bookings`.`StartDate` AS `StartDate`,`bookings`.`EndDate` AS `EndDate`,`bookings`.`ReturnDate` AS `ReturnDate` from ((`students` join `bookings` on((`students`.`SocialSecurityNumber` = `bookings`.`SocialSecurityNumber`))) join `equipment` on((`equipment`.`EquipmentId` = `bookings`.`EquipmentId`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `available_items`
--

/*!50001 DROP VIEW IF EXISTS `available_items`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `available_items` AS select `equipment`.`EquipmentId` AS `EquipmentId`,`equipment`.`Item` AS `Item`,`types`.`Category` AS `Category`,`equipment`.`Description` AS `Description`,`available_quantity`(`equipment`.`EquipmentId`,`equipment`.`TotalQuantity`) AS `AvailableQuantity` from (`equipment` join `types` on((`equipment`.`TypeId` = `types`.`TypeId`))) where (`available_quantity`(`equipment`.`EquipmentId`,`equipment`.`TotalQuantity`) > 0) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `booked_items`
--

/*!50001 DROP VIEW IF EXISTS `booked_items`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `booked_items` AS select `equipment`.`EquipmentId` AS `EquipmentId`,`equipment`.`Item` AS `Item`,`types`.`Category` AS `Category`,`equipment`.`Description` AS `Description`,sum(`active_bookings`.`Quantity`) AS `BookedQuantity` from ((`equipment` join `types` on((`equipment`.`TypeId` = `types`.`TypeId`))) join `active_bookings` on((`equipment`.`EquipmentId` = `active_bookings`.`EquipmentId`))) group by `active_bookings`.`EquipmentId` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `active_bookings`
--

/*!50001 DROP VIEW IF EXISTS `active_bookings`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `active_bookings` AS select `bookings_view`.`BookingId` AS `BookingId`,`bookings_view`.`SocialSecurityNumber` AS `SocialSecurityNumber`,`bookings_view`.`FirstName` AS `FirstName`,`bookings_view`.`LastName` AS `LastName`,`bookings_view`.`Email` AS `Email`,`bookings_view`.`PhoneNumber` AS `PhoneNumber`,`bookings_view`.`EquipmentId` AS `EquipmentId`,`bookings_view`.`Item` AS `Item`,`bookings_view`.`Quantity` AS `Quantity`,`bookings_view`.`StartDate` AS `StartDate`,`bookings_view`.`EndDate` AS `EndDate`,`bookings_view`.`ReturnDate` AS `ReturnDate` from `bookings_view` where ((`bookings_view`.`EndDate` >= curdate()) and (`bookings_view`.`ReturnDate` is null)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Dumping routines for database 'dv1663'
--
/*!50003 DROP FUNCTION IF EXISTS `available_quantity` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` FUNCTION `available_quantity`(equipment_id INT,number_of_items INT ) RETURNS int
    DETERMINISTIC
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
END ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 DROP PROCEDURE IF EXISTS `items_in_category` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `items_in_category`(type_id int)
begin 
SELECT equipment.Item,types.Category,equipment.Description, available_quantity(EquipmentId,equipment.TotalQuantity) as AvailableQuantity
FROM equipment JOIN types 
ON equipment.TypeId = types.TypeId
WHERE equipment.TypeId = type_id;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-05-27 14:00:27
