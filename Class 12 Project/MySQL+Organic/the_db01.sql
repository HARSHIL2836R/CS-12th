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
INSERT INTO `reactions` VALUES ('Halogenation or Chlorination or Bromination','Alkanes','Halogens or X2 or Chlorine or Cl2 or Bromine or Br2','Sunlight or hv','Alkyl Halide','Reaction proceeds through Free Radical Mechanism.\nProbability factors for 1, 2 and 3 degree carbons are 1:3.8:5 for Chlorination and 1:80:1600 for Bromination.\nStep 1 is Initialisation: X2 -->(hv) X* + X* .\nStep 2 is Propagation: R-H + X* --> R* + HX & R* + X2 --> R-X + X* .\nStep 3 is Termination: R* + R* --> R-R & R* + X* --> R-X .\nIf Alkane is in excess, Monohalogenated products are formed.\nIf Halogen in excess, multisubstituted products will be formed.'),('Hydrohalogenation or HX Addition','Alkene','HX or HCl or HBr','Non polar solvent: CCl4 or CHCl3 . OR Peroxide.','Alkyl Halide','Electrophilic Addition Reaction.\nAddition according to Markonikov except in case of HBr in presence of Peroxide (Antimarkonikov Addition and Free Radical Mechanism).\nFormation of Carbocation is RDS so rate depends on stability of Carbocation.\nRearrangemet of Carbocation is possible.\nMechanism: R-CH=CH2 -->(H+ from HX) R-CH|+|-CH3 -->(After Rearrangement, Attack of X-) R-CHX-CH3 \nAntimarkonikov Mechanism: R-O-O-R --> 2RO* \nRO* + HBr --> ROH + Br* \nR-CH=CH2 -->(Br*) R-CH|*|-CH2Br(More Stable Free Radical) -->(HBr) R-CH2-CH2Br + Br*'),('Allylic Chlorination','Alkene with alpha hydrogen','Chlorine or Cl2','800K','Allyl Chloride','the alpha hydrogen is replaced by chlorine.\nCH2=CH-CH3 -->(Cl2, 800K) CH2=CH-CH2-Cl \nPh-CH3 -->(Cl2, 800K) Ph-CH2-Cl'),('Bromination at Allylic Position','Alkene with alpha hydrogen','NBS or N-Bromosuccinimide','','Allyl Bromide','CH2=CH-CH3 -->(NBS) CH2=CH-CH-Br'),('Finkelstein Reaction','Alkyl Halide or R-X or RX','NaI + Actone or Non-polar solvent','Acetone as solvent','Alkyl Iodide or R-I or RI + NaX (ppt)','Proceeds through SN2 mechanism.\nNaI soluble in Acetone while NaCl and NaBr insoluble in acetone, due to high covalent character of NaI.'),('Swartz Reaction','Alkyl Halide or R-X or RX ;(X=Cl,Br,I)','AgF or Hg2F2 or CoF2 or SbF3 (aqueous)','','Alkyl Fluoride or R-F or RF + AgX (ppt)','R-X -->(AgF(aq.)) R-F + AgX (ppt) \nAlso, R-X -->(NaF + DMF) R-F + NaX ;Proceeds through SN2 mechanism \nBut, R-X -->(NaF(aq.)) NO REACTION, as ppt does not form'),('Halogenation of Alcohol','R-OH or Alcohol','conc. HX','','R-X or Alkyl Halide','Proceeds through SN1 mechanism.\nReactivity: HI and HBr react with all types of alcohols, HCl reacts only with 3degree alcohols under normal conditions, it reacts with 2 and 1 degree alcohols on heating or addition of Lucas Reagent (conc. HCl + ZnCl2), HF does nit react at all. \nReaction does not proceed if Na+X- is taken as -OH is a poor leaving group. \n Mechanism: R-OH -->(H+) R-OH2|+| --> R|+| -->(X-) R-X'),('Halogenation using PX3','R-OH','PX3 or phosphorus trihalide','','R-X or Alkyl Halide + H3PO3 Phosphorous Acid','X = Cl, Br, I'),('Halogenation using PX5','R-OH or Alcohol','PX5 or Phosphorus Pentahalide','','R-X or Alkyl Halide + HX or hydrogen halide + POX3 or Phosphoryl Halide','X = Cl, Br'),('Darzens Process','R-OH or Alcohol','SOCl2 or Thionyl Chloride','','R-Cl or Alkyl Chloride + SO2 or Sulphur Dioxide (gas) + HCl or Hydrogen Chloride (gas)','Retention of Configuration. SNi mechanism.\nBut in presence of pyridene, Inversion of Configuration, as pyridine acting as a base generates Cl- Nucleophile to attack intermediate R-O-SOCl.\nMechanism: R-OH -->(SOCl2) R-OH|+|-S{(Cl)2}-O|-| -->(-HCl) R-O-SOCl --> R-Cl + SO2'),('Hundsdicker Reaction','R-COOH or Carboxylic Acid','moist Ag2O (AgOH) + Br2 + heat','','R-Br + CO2 (gas) + AgBr (ppt)','Proceeds through Free Radical Mechanism whose finals Steps are like: R-CO-O-Br --> R-CO-O* + Br* --> R* + CO2 +Br* --> R-Br \nF2 and Cl2 does not give this rx as they have high BDE and form less soluble ppt \nIn case of I2, reaction is call Birnbaum-Simonini Reaction and major product is ester \nMechanism: R-CO-O-I --> R-CO-O* + I* \nWHERE I* + I* --> I2 (fast) \nAND R-CO-O* --> R* + CO2 (slow) ; R* + R-CO-O* --> R-CO-OR + R-R \n 3 degree free radicals give disproportionation products 2 (CH3)3C* --> (CH3)3CH + CH2=C(CH3)2'),('Gattermann-Koch Formylation','Benzene or Aromatic Compounds','Carbon Monoxide or CO','HCl or hydrochloric acid + Annhydrous Aluminium Chloride or AlCl3 (OR) Copper(I) Chloride or CuCl','Benzaldehyde or Formyl Substituted Aromatic Compound','Proceeds through Electrophilic Substitution mechanism on Aromatic Compounds. Mechanism can be written as: C|-|O|+| -->(HCl) H-CO|+| <--> H-C|+|=O -->(Cl-) Cl-CH=O -->(AlCl3) Cl-CH=O---AlCl3 --> H-C|+|=O');
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

-- Dump completed on 2022-11-26  0:12:01
