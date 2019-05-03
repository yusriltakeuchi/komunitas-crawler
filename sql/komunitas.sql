-- --------------------------------------------------------
-- Host:                         localhost
-- Server version:               5.7.24 - MySQL Community Server (GPL)
-- Server OS:                    Win64
-- HeidiSQL Version:             9.5.0.5332
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Dumping database structure for komunitas
CREATE DATABASE IF NOT EXISTS `komunitas` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `komunitas`;

-- Dumping structure for table komunitas.category
CREATE TABLE IF NOT EXISTS `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table komunitas.details
CREATE TABLE IF NOT EXISTS `details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(300) DEFAULT NULL,
  `address` text,
  `city` varchar(100) DEFAULT NULL,
  `region` varchar(100) DEFAULT NULL,
  `postal_code` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `description` text,
  `website` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=461 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table komunitas.detail_list
CREATE TABLE IF NOT EXISTS `detail_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_details` int(11) NOT NULL DEFAULT '0',
  `id_category` int(11) NOT NULL DEFAULT '0',
  `id_social` int(11) NOT NULL DEFAULT '0',
  `id_tag` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=439 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table komunitas.social_media
CREATE TABLE IF NOT EXISTS `social_media` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=655 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
-- Dumping structure for table komunitas.tag
CREATE TABLE IF NOT EXISTS `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=716 DEFAULT CHARSET=latin1;

-- Data exporting was unselected.
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
