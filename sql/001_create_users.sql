DROP TABLE IF EXISTS Users;

CREATE TABLE Users (
	userId VARCHAR(5) NOT NULL UNIQUE,
    username VARCHAR(15) NOT NULL UNIQUE,
    user_role CHAR (10),
    vip CHAR(3),
    user_money FLOAT(8),
    amount_spent FLOAT(8),
    user_warnings INT(1),
    user_compliments INT(1),
    is_blacklisted CHAR(3),
    PRIMARY KEY (userId, username));
    
    
INSERT INTO Users VALUES (00001, "User-1", 'Manager', 'NO', 200, 150, 0, 5, 'NO');
INSERT INTO Users VALUES (00002, "User-2", 'Chef', 'NO', 34, 13, 0, 2, 'NO');
INSERT INTO Users VALUES (00003, "User-3", 'Chef', 'NO', 44, 76, 1, 1, 'NO');
INSERT INTO Users VALUES (00004, "User-4", 'Delivery', 'NO', 22, 65, 1, 0, 'NO');
INSERT INTO Users VALUES (00005, "User-5", 'Delivery', 'NO', 33, 90, 2, 2, 'NO');
INSERT INTO Users VALUES (00006, "User-6", 'Customer', 'YES', 435, 245, 0, 0, 'NO');
INSERT INTO Users VALUES (00007, "User-7", 'Customer', 'NO', 55, 87, 0, 0, 'NO');

SELECT * FROM Users;
