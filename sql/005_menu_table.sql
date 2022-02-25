DROP TABLE IF EXISTS menu ;

CREATE TABLE IF NOT EXISTS menu (
  `id` INT NOT NULL AUTO_INCREMENT,
  `chefID` INT NOT NULL,
  `dishID` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `chefID_idx` (`chefID` ASC) VISIBLE,
  INDEX `dishID_idx` (`id` ASC, `dishID` ASC) VISIBLE,
  CONSTRAINT `fk_chefID`
    FOREIGN KEY (`chefID`)
    REFERENCES `employees` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_dishID`
    FOREIGN KEY (`id` , `dishID`)
    REFERENCES `dish` (`id` , `id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;