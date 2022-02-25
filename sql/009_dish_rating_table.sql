DROP TABLE IF EXISTS dishRating ;

CREATE TABLE IF NOT EXISTS dishRating (
  `id` INT NOT NULL AUTO_INCREMENT,
  `rating` INT NOT NULL,
  `comment` VARCHAR(45) NULL,
  `custID` INT NOT NULL,
  `dishID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_custID_idx` (`custID` ASC) VISIBLE,
  INDEX `dishID_idx` (`dishID` ASC) VISIBLE,
  CONSTRAINT `fk_custID`
    FOREIGN KEY (`custID`)
    REFERENCES `customers` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dishID`
    FOREIGN KEY (`dishID`)
    REFERENCES `dish` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

