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

INSERT INTO employees VALUES (00001, "User-1", 'Manager', 1);
INSERT INTO employees VALUES (00002, "User-2", 'Chef', 1);
INSERT INTO employees VALUES (00003, "User-3", 'Chef', 1);
INSERT INTO employees VALUES (00004, "User-4", 'Delivery', 1);
INSERT INTO employees VALUES (00005, "User-5", 'Delivery', 1);