INSERT INTO businesses (Name, Address, Phone) VALUES ( "Moe's Tavern", '555 5th Avenue', '(212)-867-5309');
INSERT INTO employees VALUES (1, "Tracy", "abc@123.com" , "",'Manager', 1);
INSERT INTO employees VALUES (2, "Stefan", "joe@shmoe.org" ,"Bobbyscar@yahoo.com" , 'Chef', 1);
INSERT INTO employees VALUES (3, "Rachel", "a@b.c" ,"3",'Chef', 1);
INSERT INTO employees VALUES (4, "Bob", "hi@there.com" ,"4",'Delivery', 1);
INSERT INTO employees VALUES (5, "Jeffrey", "blah@blah.edu" ,"5", 'Delivery', 1);

INSERT INTO customers VALUES (1, "Jolene", "why@dahell.com", "amihere" ,0);
INSERT INTO customers VALUES (2, "Nathaniel", "jimmytwoshoes@aol.com","jimmy" ,1);
INSERT INTO customers VALUES (3, "Tom", "Tom@Tom.Tom", "Tom",0);
INSERT INTO customers VALUES (4, "Angelica","ahhh@1.2", "3",0);
INSERT INTO customers VALUES (5, "Brady", "8@superbowl.rings","easy" ,1);
INSERT INTO customers VALUES (6, "DATBOI", "bigboi@aol.com", "password", 0);

INSERT INTO dish VALUES (1, "Caesar Salad", 'a tossed salad made of romaine, garlic, anchovies, and croutons and dressed with olive oil, coddled egg, lemon juice, and grated cheese. ', 1);
INSERT INTO dish VALUES (2, "Flaming Moe", 'The signature specialty drink of Springfield', 1);
INSERT INTO dish VALUES (3, "Chicken Wings", 'Fresh chicken wings that comes with a side dip of your choice.', 1);
INSERT INTO dish VALUES (4, "Draft Beer", 'Choose from Duff or Duff Lite.', 1);
INSERT INTO dish VALUES (5, "Mr.Teeny", 'Lemonade, pineapple juice, and Blue Curaçao syrup. Freshly prepared and served with a specialty garnish.', 1);
INSERT INTO dish VALUES (6, "Burgers and Fries", 'A juicy hamburger topped with lettuce, pickles, onions, mayo and ketchup and a side of fries.', 1);
INSERT INTO dish VALUES (7, "Birria Tacos", ' Topped with cilantro, onion, a spicy red sauce and a wedge of lime.', 1);
INSERT INTO dish VALUES (8, "Pizza", 'its just pizza.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Mac n Cheese", 'Its mac n cheese just the way you like it.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Chicken Parmesan", 'Boneless chicken breast salt and peppered, sprinkled with bread crumbs and grated Parmesan cheese, then soaked in tomato sauce.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Egg Salad", 'Chopped eggs stirred in a bowl with mayonnaise, mustard and green onion. Seasoned with salt, pepper and paprika', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Garlic Chicken Fried Rice", 'chicken fried rice with peppers, onions and garlic. Stirred in soy sauce, rice vinegar and peas. ', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Spaghetti Aglio e Olio", 'Cooked spaghetti stirred with red pepper flakes, black pepper, salt, olive oil, Italian parsley, toasted garlic, and topped with Parmigiano-Reggiano cheese.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Chicken Cordon Bleu ", '', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Grilled Cheese", 'Bread, butter, american cheese on a grill. An American classic.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Sloppy Joe", 'Ground beef, onion, green pepper, and ketchup are seasoned with garlic powder, yellow mustard, brown sugar and salt&pepper (optional).', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Steak Nachos", 'Steak nachos and beans sprinkled with grated cheese, diced ripe avocado, diced onions, diced tomatoes, and diced jalapenos, sour cream and chopped cilantro.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Chocolate Cake", 'A slice of cake from the cake factory across the street. (Dont tell them about this)', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Tres Leches (Three Milk Cake)", 'Is a sponge cake soaked in a mixture of three kinds of milk, topped with whipped cream and strawberries (optional).', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Roasted Rack of Lamb", 'A rack of lamb seared, salt and peppered, and encrusted with Dijon mustard, garlic, bread crumbs and fresh rosemary.', 1);

INSERT INTO menu VALUES (1, 2, 1);
INSERT INTO menu VALUES (2, 3, 1);
INSERT INTO menu VALUES (3, 3, 1);
INSERT INTO menu VALUES (4, 2, 1);
INSERT INTO menu VALUES (5, 2, 1);


-- INSERT INTO orders VALUES (1, "$24.50", NULL, 3, 1);
-- INSERT INTO orders VALUES (2, "$11.00", NULL, 3, 1);
-- INSERT INTO orders VALUES (3, "$4.19", NULL, 3, 1);

-- INSERT INTO orderLineItem VALUES (1, 8, 2, 3);
-- INSERT INTO orderLineItem VALUES (1, 1, 2, 3);
-- INSERT INTO orderLineItem VALUES (3, 3, 2, 3);
-- INSERT INTO orderLineItem VALUES (4, "Pizza", 2, 3);
-- INSERT INTO orderLineItem VALUES (5, "Pizza", 2, 3);

 INSERT INTO dishRating VALUES (1, 5, "Wheres the tip jar that grilled chee smacked", 2, 15);
 INSERT INTO dishRating VALUES (2, 4, "not bad, needed more salt", 2, 4);
 INSERT INTO dishRating VALUES (3, 4, "wheres da lamb sauce", 1, 20);
 INSERT INTO dishRating VALUES (4, 5, "Pizza was fire", 4, 8);
 INSERT INTO dishRating VALUES (5, 3, "Pizza was meh", 3, 8);


 INSERT INTO menuDishes VALUES(1,1,"$7.99");
 INSERT INTO menuDishes VALUES(1,3,"$8.99");
 INSERT INTO menuDishes VALUES(2,2,"$4.19");
 INSERT INTO menuDishes VALUES(2,3,"$9.99");
 INSERT INTO menuDishes VALUES(2,8,"$3.00");