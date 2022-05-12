INSERT INTO businesses (Name, Address, Phone) VALUES ( "Moe's Tavern", '555 5th Avenue', '(212)-867-5309');
INSERT INTO employees VALUES (1, "Tracy", "abc@123.com" , "",'Manager', 1);
INSERT INTO employees VALUES (2, "Stefan", "joe@shmoe.org" ,"Bobbyscar@yahoo.com" , 'Chef', 1);
INSERT INTO employees VALUES (3, "Rachel", "a@b.c" ,"3",'Chef', 1);
INSERT INTO employees VALUES (4, "Bob", "hi@there.com" ,"4",'Delivery', 1);
INSERT INTO employees VALUES (5, "Jeffrey", "blah@blah.edu" ,"5", 'Delivery', 1);

INSERT INTO dish VALUES (1, "Caesar Salad", 'a tossed salad made of romaine, garlic, anchovies, and croutons and dressed with olive oil, coddled egg, lemon juice, and grated cheese. ', 1);
INSERT INTO dish VALUES (2, "Flaming Moe", 'The signature specialty drink of Springfield', 1);
INSERT INTO dish VALUES (3, "Chicken Wings", 'Fresh chicken wings that comes with a side dip of your choice: Hot Buffalo, Honey BBQ or sweet Asian Chili sauce.', 1);
INSERT INTO dish VALUES (4, "Draft Beer", 'Choose from Duff or Duff Lite.', 1);
INSERT INTO dish VALUES (5, "Mr.Teeny", 'Lemonade, pineapple juice, and Blue Curaçao syrup. Freshly prepared and served with a specialty garnish.', 1);
INSERT INTO dish VALUES (6, "Bacon Cheeseburger", 'A handcrafted all-beef patty topped with two slices of American cheese and two strips of Applewood-smoked bacon. Served with lettuce, tomato, onion and pickles on a Brioche bun with fries.', 1);
INSERT INTO dish VALUES (7, "Birria Tacos", ' Topped with cilantro, onion, a spicy red sauce and a wedge of lime.', 1);
INSERT INTO dish VALUES (8, "Spinach & Artichoke dip", 'Creamy spinach and artichoke dip topped with melted Parmesan cheese. Served with freshly made white corn tortilla chips and our chipotle lime salsa.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Strawberry Balsamic Chicken Salad", 'Mixed greens served with lemon olive oil vinaigrette, tomatoes, red onions and fresh strawberries. Topped with grilled chicken, sliced almonds and balsamic glaze.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Fountain Drinks", 'Your choice of Sprite, Coca Cola, Diet Coke, Pepsi, Brisk Iced Tea, and Fanta.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Egg Salad", 'Chopped eggs stirred in a bowl with mayonnaise, mustard and green onion. Seasoned with salt, pepper and paprika', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Baby Back Ribs", 'Full Rack. Slow-cooked to fall off the bone tenderness. Slathered with your choice of sauce: - Honey BBQ sauce - Sweet Asian Chili sauce', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Spaghetti Aglio e Olio", 'Cooked spaghetti stirred with red pepper flakes, black pepper, salt, olive oil, Italian parsley, toasted garlic, and topped with Parmigiano-Reggiano cheese.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("French Onion Soup", 'Prepared with beef stock and caramelized onions. Top with croutons covered in melty Gruyere and Parmesan cheese.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Blue Ribbon Brownie", 'Chunks of dark chocolate, nuts & hot fudge. Two scoops of vanilla ice cream.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Classic Broccoli Chicken Alfredo", 'Juicy grilled chicken is served warm on a bed of fettuccine pasta tossed with broccoli and rich Alfredo sauce and topped with Parmesan cheese.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Steak Nachos", 'Steak nachos and beans sprinkled with grated cheese, diced ripe avocado, diced onions, diced tomatoes, and diced jalapenos, sour cream and chopped cilantro.', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Chocolate Cake", 'A slice of cake from the cake factory across the street. (Dont tell them about this)', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Tres Leches (Three Milk Cake)", 'Is a sponge cake soaked in a mixture of three kinds of milk, topped with whipped cream and strawberries (optional).', 1);
INSERT INTO dish (name, description, bizID) VALUES ("Sizzlin' Caramel Apple Blondie", 'Cinnamon apples surround our famous butter pecan blondie topped with vanilla ice cream, sizzled and drizzled with caramel sauce and a sprinkle of candied pecans.', 1);


INSERT INTO menu VALUES (1, 2, 1);
INSERT INTO menu VALUES (2, 3, 1);
INSERT INTO menu VALUES (3, 3, 1);
INSERT INTO menu VALUES (4, 2, 1);
INSERT INTO menu VALUES (5, 2, 1);

INSERT INTO customers VALUES (1, "Jolene", "why@dahell.com", "amihere" ,0);
INSERT INTO customers VALUES (2, "Nathaniel", "jimmytwoshoes@aol.com","jimmy" ,1);
INSERT INTO customers VALUES (3, "Tom", "Tom@Tom.Tom", "Tom",0);
INSERT INTO customers VALUES (4, "Angelica","ahhh@1.2", "3",0);
INSERT INTO customers VALUES (5, "Brady", "8@superbowl.rings","easy" ,1);
INSERT INTO customers VALUES (6, "DATBOI", "bigboi@aol.com", "password", 0);

INSERT INTO orders VALUES (1, "$24.50", NULL, 3, 1); 
INSERT INTO orders VALUES (2, "$11.00", NULL, 2, 1);
INSERT INTO orders VALUES (3, "$4.19", NULL, 4, 1);

INSERT INTO orderLineItem VALUES (1, 1, "7.99", NOT NULL, "7.99", 1, 14);
INSERT INTO orderLineItem VALUES (2, 2, "7.99", NOT NULL, "7.99", 1, 1);
INSERT INTO orderLineItem VALUES (3, 1, "7.99", NOT NULL, "4.99", 2, 11);
INSERT INTO orderLineItem VALUES (4, 1, "7.99", NOT NULL, "11.99", 2, 14);
INSERT INTO orderLineItem VALUES (5, 1, "7.99", NOT NULL, "8.50", 3, 18);

INSERT INTO dishRating VALUES (1, 5, "Wheres the tip jar that grilled chee smacked", 2, 15);
INSERT INTO dishRating VALUES (2, 4, "not bad, needed more salt", 2, 4);
INSERT INTO dishRating VALUES (3, 4, "wheres da lamb sauce", 1, 20);
INSERT INTO dishRating VALUES (4, 5, "Pizza was fire", 4, 8);
INSERT INTO dishRating VALUES (5, 3, "Pizza was meh", 3, 8);


INSERT INTO menuDishes VALUES(1,8,"$10.00");
INSERT INTO menuDishes VALUES(1,3,"$8.00");
INSERT INTO menuDishes VALUES(1,7,"$4.00");
INSERT INTO menuDishes VALUES(1,17,"$12.00");

INSERT INTO menuDishes VALUES(2,16,"$18.00");
INSERT INTO menuDishes VALUES(2,12,"$29.00");
INSERT INTO menuDishes VALUES(2,6,"$13.50");
INSERT INTO menuDishes VALUES(2,13,"$17.00");

INSERT INTO menuDishes VALUES(3,1,"$9.00");
INSERT INTO menuDishes VALUES(3,11,"$11.00");
INSERT INTO menuDishes VALUES(3,14,"$9.50");
INSERT INTO menuDishes VALUES(3,9,"$12.00");

INSERT INTO menuDishes VALUES(4,19,"$10.00");
INSERT INTO menuDishes VALUES(4,18,"$8.00");
INSERT INTO menuDishes VALUES(4,20,"$12.00");
INSERT INTO menuDishes VALUES(4,15,"$10.00");

INSERT INTO menuDishes VALUES(5,10,"$3.00");
INSERT INTO menuDishes VALUES(5,2,"$7.00");
INSERT INTO menuDishes VALUES(5,5,"$10.00");
INSERT INTO menuDishes VALUES(5,4,"$8.50");