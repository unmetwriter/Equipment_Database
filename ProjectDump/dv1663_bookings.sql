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
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `BookingId` int NOT NULL AUTO_INCREMENT,
  `SocialSecurityNumber` varchar(13) NOT NULL,
  `EquipmentId` int NOT NULL,
  `Quantity` int NOT NULL,
  `StartDate` date DEFAULT NULL,
  `EndDate` date DEFAULT NULL,
  `ReturnDate` date DEFAULT NULL,
  PRIMARY KEY (`BookingId`),
  KEY `SocialSecurityNumber` (`SocialSecurityNumber`),
  KEY `EquipmentId` (`EquipmentId`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`SocialSecurityNumber`) REFERENCES `students` (`SocialSecurityNumber`),
  CONSTRAINT `bookings_ibfk_2` FOREIGN KEY (`EquipmentId`) REFERENCES `equipment` (`EquipmentId`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,'01-01-02-0000',1,1,'2023-05-01','2023-05-08','2023-05-08'),(2,'02-01-02-0000',2,1,'2024-01-01','2023-01-20','2023-01-20'),(3,'04-01-02-0000',3,1,'2024-05-01','2024-05-08',NULL),(4,'03-01-02-0000',4,2,'2024-05-03','2024-05-08','2024-05-10'),(5,'03-01-02-0000',5,15,'2024-05-03','2024-05-08','2024-05-10'),(6,'05-01-02-0000',5,3,'2024-05-03','2024-05-08',NULL),(7,'0206238131',1,1,'2024-05-23','2025-05-23','2024-05-25'),(8,'03-01-02-0000',6,2,'2024-06-01','2024-06-10','2024-05-27'),(9,'04-01-02-0000',7,3,'2024-06-05','2024-06-15',NULL),(10,'05-01-02-0000',8,4,'2024-06-08','2024-06-18',NULL),(11,'06-01-02-0000',9,2,'2024-06-10','2024-06-20',NULL),(12,'07-01-02-0000',10,3,'2024-06-15','2024-06-25',NULL),(13,'0206238131',3,4,'2024-05-27','2025-05-27',NULL);
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `stop_booking_insertion_if_already_exists` BEFORE INSERT ON `bookings` FOR EACH ROW begin
IF (exists(SELECT 1 FROM bookings WHERE (SocialSecurityNumber= new.SocialSecurityNumber AND EquipmentId = new.EquipmentId AND StartDate = new.StartDate AND EndDate =new.EndDate  ) )) THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = "The booking already exists.";
END IF;
end */;;
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
