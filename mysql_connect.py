import mysql.connector

# cnx = mysql.connector.connect(user='sql5475223', password='Z2QSXniDNP',
#                               host='sql5.freesqldatabase.com',
#                               database='sql5475223')
conn = mysql.connector.connect(user='root', password='MyDBserver1998', host='localhost', database='test_schema')


class Menu:
    def __init__(self, id, bizID, chefID, dishes = []):
        self._id = id
        self._name = None
        self._bizID = bizID
        self._chefID = chefID
        self._dishes = dishes
    
    @property
    def id(self):
        return f'{self._id}'

    @property
    def name(self):
        return f'{self._name}'

    @property
    def bizID(self):
        return f'{self._bizID}'

    @property
    def chef(self):
        return f'{self._chefID}'

    @property
    def dishes(self):
        return self._dishes

    def setDishes(self, dishes):
        self._dishes = dishes 

class Dish:
    def __init__(self, id, name, description, bizID):
        self._id = id
        self._name = name
        self._description = description
        self._bizID = bizID

    @property
    def id(self):
        return f'{self._id}'

    @property
    def name(self):
        return f'{self._name}'

    @property
    def desc(self):
        return f'{self._description}'

    @property
    def bizID(self):
        return f'{self._bizID}'


def getDishes(cnx, bizID)  :
    dishes = []
    c = cnx.cursor()
    c.execute(f'select id, name, description from dish where bizID = {bizID}')
    for row in c :
        d = Dish(row[0], row[1], row[2], bizID)
        print(d.id, " : ", d.name, " - ", d.desc)
        dishes.append(d) 
    c.close()
    return dishes

# d = getDishes( conn, 1)
# print(d)


def getMenu(cnx, bizID, menuID) -> Menu:
    c = cnx.cursor()
    c.execute(f'SELECT id, businessID, chefID FROM menu WHERE businessID = {bizID} AND id = {menuID}')
    chefID = None
    for row in c :
        chefID = row[2]
        break
    c.close()
    m = Menu(menuID, bizID, chefID)
    x = getDishes(cnx, bizID)
    m.setDishes(x)
    return m

m = getMenu(conn, 1, 1)
print("Got a menu # ", m.id, " Chef# : ",  m.chef)
print("Dishes are :\n-----------\n")
for dish in m.dishes :
    print(dish.id, " : ", dish.name, " \t ", dish.desc)
