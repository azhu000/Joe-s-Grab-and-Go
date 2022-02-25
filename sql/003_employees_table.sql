DROP TABLE IF EXISTS `employees` ;

CREATE TABLE IF NOT EXISTS `employees` (
  `id`  INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `role` VARCHAR(45) NOT NULL,
  `bizID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `bizID_idx` (`bizID` ASC) VISIBLE,
  CONSTRAINT `fk_bizID`
    FOREIGN KEY (`bizID`)
    REFERENCES `businesses` (`id`)
    ON UPDATE CASCADE);