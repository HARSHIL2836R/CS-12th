-- MySQL dump 10.13  Distrib 5.7.40, for Win64 (x86_64)
--
-- Host: localhost    Database: Organic_chem
-- ------------------------------------------------------
-- Server version	5.7.40-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reactions`
--

DROP TABLE IF EXISTS `reactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reactions` (
  `Name` tinytext NOT NULL,
  `Reactant` tinytext,
  `Reagent` tinytext NOT NULL,
  `Conditions` tinytext,
  `Product` tinytext,
  `Remarks` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reactions`
--

LOCK TABLES `reactions` WRITE;
/*!40000 ALTER TABLE `reactions` DISABLE KEYS */;
INSERT INTO `reactions` VALUES ('Halogenation or Chlorination or Bromination','Alkanes','Halogens or Chlorine or Bromine','Sunlight or hv','Alkyl Halide','Reaction proceeds through Free Radical Mechanism.\nProbability factors for 1, 2 and 3 degree carbons are 1:3.8:5 for Chlorination and 1:80:1600 for Bromination.\nStep 1 is Initialisation: X2 -->(hv) X* + X* .\nStep 2 is Propagation: R-H + X* --> R* + HX & R* + X2 --> R-X + X* .\nStep 3 is Termination: R* + R* --> R-R & R* + X* --> R-X .\nIf Alkane is in excess, Monohalogenated products are formed.\nIf Halogen in excess, multisubstituted products will be formed.'),('Hydrohalogenation or HX Addition','Alkene','HX or HCl or HBr','Non polar solvent: CCl4 or CHCl3 . OR Peroxide.','Alkyl Halide','Electrophilic Addition Reaction.\nAddition according to Markonikov except in case of HBr in presence of Peroxide (Antimarkonikov Addition and Free Radical Mechanism).\nFormation of Carbocation is RDS so rate depends on stability of Carbocation.\nRearrangemet of Carbocation is possible.\nMechanism: R-CH=CH2 -->(H+ from HX) R-CH|+|-CH3 -->(After Rearrangement, Attack of X-) R-CHX-CH3 \nAntimarkonikov Mechanism: R-O-O-R --> 2RO* \nRO* + HBr --> ROH + Br* \nR-CH=CH2 -->(Br*) R-CH|*|-CH2Br(More Stable Free Radical) -->(HBr) R-CH2-CH2Br + Br*'),('Allylic Chlorination','Alkene with alpha hydrogen','Chlorine or Cl2','800K','Allyl Chloride','the alpha hydrogen is replaced by chlorine.\nCH2=CH-CH3 -->(Cl2, 800K) CH2=CH-CH2-Cl \nPh-CH3 -->(Cl2, 800K) Ph-CH2-Cl');
/*!40000 ALTER TABLE `reactions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-17 23:39:09
