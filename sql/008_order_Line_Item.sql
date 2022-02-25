DROP TABLE IF EXISTS orderLineItem ;

CREATE TABLE IF NOT EXISTS orderLineItem (
  `id` INT NOT NULL AUTO_INCREMENT,
  `quantity` VARCHAR(45) NOT NULL,
  `subtotal` VARCHAR(45) NOT NULL,
  `discount` VARCHAR(45) NULL,
  `total` VARCHAR(45) NOT NULL,
  `orderID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_orderID_idx` (`orderID` ASC) VISIBLE,
  CONSTRAINT `fk_orderID`
    FOREIGN KEY (`orderID`)
    REFERENCES `orders` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;