DROP TABLE IF EXISTS `businesses` ;

CREATE TABLE IF NOT EXISTS `businesses` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(255) NOT NULL,
  `Phone` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
;

    
INSERT INTO businesses (Name, Address, Phone) VALUES ( "Moe's Tavern", '555 5th Avenue', '(212)-867-5309');

