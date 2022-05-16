-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';



-- -----------------------------------------------------
-- Table .`businesses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `businesses` ;

CREATE TABLE IF NOT EXISTS `businesses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  `Phone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`));




-- -----------------------------------------------------
-- Table `employees`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `employees` ;

CREATE TABLE IF NOT EXISTS `employees` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  `bizID` INT NOT NULL,
  INDEX `bizID_idx` (`bizID` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE,
  CONSTRAINT `fk_bizID`
    FOREIGN KEY (`bizID`)
    REFERENCES `businesses` (`id`)
    ON UPDATE CASCADE);


-- -----------------------------------------------------
-- Table `dish`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dish` ;

CREATE TABLE IF NOT EXISTS `dish` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `bizID` INT NOT NULL,
  `url` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE,
  INDEX `fk_bizID_idx` (`bizID` ASC) VISIBLE,
  CONSTRAINT `fk_biz`
    FOREIGN KEY (`bizID`)
    REFERENCES `businesses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table .`menu`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `menu` ;

CREATE TABLE IF NOT EXISTS `menu` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `chefID` INT NOT NULL,
  `businessID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `chefID_idx` (`chefID` ASC) VISIBLE,
  INDEX `fk_businessID_idx` (`businessID` ASC) VISIBLE,
  CONSTRAINT `fk_chefID`
    FOREIGN KEY (`chefID`)
    REFERENCES `employees` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_businessID`
    FOREIGN KEY (`businessID`)
    REFERENCES `businesses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table .`customers`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `customers` ;

CREATE TABLE IF NOT EXISTS `customers` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `wallet` FLOAT(16,2) NOT NULL DEFAULT 0,
  `isVIP` TINYINT NOT NULL DEFAULT 0,
  `warning` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `password_UNIQUE` (`password` ASC) VISIBLE);




-- -----------------------------------------------------
-- Table .`orders`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `orders` ;

CREATE TABLE IF NOT EXISTS `orders` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `total` FLOAT(16,2) NOT NULL,
  `DeliveryTime` VARCHAR(45) NULL,
  `Active` TINYINT NOT NULL DEFAULT 1,
  `custID` INT NOT NULL,
  `bizID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_custID_idx` (`custID` ASC) VISIBLE,
  INDEX `fk_bizID_idx` (`bizID` ASC) VISIBLE,
  CONSTRAINT `fk_custID`
    FOREIGN KEY (`custID`)
    REFERENCES `customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_biznizID`
    FOREIGN KEY (`bizID`)
    REFERENCES `businesses` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table .`orderLineItem`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `orderLineItem` ;

CREATE TABLE IF NOT EXISTS `orderLineItem` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` FLOAT(16,2) NOT NULL,
  `subtotal` FLOAT(16,2) NOT NULL,
  `discount` VARCHAR(45) NULL,
  `total` FLOAT(16,2) NOT NULL,
  `orderID` INT NOT NULL,
  `DishOrdered` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_orderID_idx` (`orderID` ASC) VISIBLE,
  INDEX `fk_DishOrdered_idx` (`DishOrdered` ASC) VISIBLE,
  CONSTRAINT `fk_orderID`
    FOREIGN KEY (`orderID`)
    REFERENCES `orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DishOrdered`
    FOREIGN KEY (`DishOrdered`)
    REFERENCES `dish` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table .`dishRating`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `dishRating` ;

CREATE TABLE IF NOT EXISTS `dishRating` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rating` INT NOT NULL,
  `comment` VARCHAR(45) NULL,
  `custID` INT NOT NULL,
  `dishID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_custID_idx` (`custID` ASC) VISIBLE,
  INDEX `dishID_idx` (`dishID` ASC) VISIBLE,
  CONSTRAINT `fk_customerID`
    FOREIGN KEY (`custID`)
    REFERENCES `customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dish`
    FOREIGN KEY (`dishID`)
    REFERENCES `dish` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


-- -----------------------------------------------------
-- Table .`menuDishes`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `menuDishes` ;

CREATE TABLE IF NOT EXISTS `menuDishes` (
  `id` INT NOT NULL,
  `MenuDishID` INT NOT NULL,
  `price` FLOAT(16,2) NOT NULL,
  `VIP` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`, `MenuDishID`),
  CONSTRAINT `fk_MenuDishID`
    FOREIGN KEY (`id`)
    REFERENCES `dish` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ID`
    FOREIGN KEY (`id`)
    REFERENCES `menu` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;