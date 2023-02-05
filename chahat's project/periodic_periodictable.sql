-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: periodic
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `periodictable`
--

DROP TABLE IF EXISTS `periodictable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `periodictable` (
  `Symbol` char(3) DEFAULT NULL,
  `Name` varchar(27) DEFAULT NULL,
  `Atomic_No` int DEFAULT NULL,
  `Atomic_Mass` float DEFAULT NULL,
  `Valency` int DEFAULT NULL,
  `Density` float DEFAULT NULL,
  `Boiling_Point` float DEFAULT NULL,
  `Melting_Point` float DEFAULT NULL,
  `Electronegativity` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodictable`
--

LOCK TABLES `periodictable` WRITE;
/*!40000 ALTER TABLE `periodictable` DISABLE KEYS */;
INSERT INTO `periodictable` VALUES ('Es','Einsteinium',99,252,3,8.84,1269,1133,1.3),('H','Hydrogen',1,1,1,0.00008988,20.28,14.01,2.2),('Sc','Scandium',21,45,3,2.99,3109,1814,1.36),('Ge','Germanium',32,73,4,5.907,3106,1211.4,2.01),('Cd','Cadmium',48,112,2,8.69,1040,594.22,1.69),('Xe','Xenon',54,131,0,0.005887,165.03,161.4,2.6),('Ho','Holmium',67,165,3,8.795,2993,1734,1.23),('Os','Osmium',76,190,4,22.61,5285,3306,2.2),('Ra','Radium',88,227,2,5.5,2010,973,0.9),('Cm','Curium',96,247,3,13.51,3383,1613,1.28),('Es','Einsteinium',99,252,3,8.84,1269,1133,1.3);
/*!40000 ALTER TABLE `periodictable` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-02 16:58:03
