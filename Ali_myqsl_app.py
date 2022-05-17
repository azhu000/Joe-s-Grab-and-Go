#from crypt import methods
#from ctypes import addressof

from ast import Delete
from doctest import TestResults
from functools import wraps
from getopt import gnu_getopt
import random
from re import I
from unicodedata import name
import bcrypt
from click import password_option
from flask import Flask, g, redirect, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LOGIN_MESSAGE, UserMixin, login_user, LoginManager, login_required, logout_user,current_user
from flask_wtf import FlaskForm
from sqlalchemy import ForeignKey
from sqlalchemy import *
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

#Initial Comments
# To run this code, i have modified both login.html and register.html by changing form.username to form.name
# This code requires you to install pymysql. 
# pip install pymysql
# It is a modified version of anson's code, capable of running with MySQL.
# To use your own local database, change the "conn" variable to your own information in this format:
# conn = "mysql+pymysql://{0}:{1}@{2}/{3}" 
# 0 = the username of your DB
# 1 = the password of your DB
# 2 = the host/localhost of your DB (its usually localhost if you arent hosting it online)
# 3 = the name of your DB


conn = "mysql+pymysql://root:john1715@localhost/test_schema"

#Creating the app which the Flsk app will run off
app = Flask(__name__)
bcrypt = Bcrypt(app)
#Setting up database
app.config['SQLALCHEMY_DATABASE_URI'] = conn
app.config['SECRET_KEY'] = 'secretkey'
db = SQLAlchemy(app)

#Login management
#loading users based on id's from the database
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

menu_tags = ["Appetizers", "Entrees", "Soup & Salad", "Dessert", "Beverages"]
vip_tags = ["Special Boi menuuuuuu les goo"]

# loads the user id which is stored
# This does not work like it should. It checks for the ID of the user and if it exists in customer
# else it will check in employees. 
# Both tables have the same IDs, so the else statement will never trigger. 
# Would need to check by email, but I am not sure at all what is actually being passed in. 
@login_manager.user_loader
def load_user(id):
    if customers.query.get(int(id)):
        return customers.query.get(int(id))
    else:
        return employees.query.get(int(id))



# setting up database ids
# Note: not sure if its more comprehensive to list the relationships between classes
#  in the parent class or the child class. For now its in the parent class.
# I have no clue if the foreign keys will work. That is still to be tested.

class businesses(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name = db.Column(db.String(45), nullable = False)
    address = db.Column(db.String(255), nullable = False)
    phone = db.Column(db.Integer, nullable = False)
    employee = db.relationship('employees', backref='businesses')
    dishes = db.relationship('dish', backref='businesses')
    order = db.relationship('orders', backref='businesses')
    #might be possible for a single relationship() to define two children 
    # employee = db.relationship('employees', secondary=dish, backref='businesses')


# This class is missing a way to get specific roles. Something like:
# SELECT employees WHERE role = chef, so that it can be referenced by 'menu' class.
# Might also need UserMixin for the class if we implement employees similar to customers.
class employees(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name = db.Column(db.String(45), nullable = False)
    email = db.Column(db.String(45), nullable = False)
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(45), nullable = False)
    isBlacklisted = db.Column(db.Integer, nullable = True, default = 0)
    bizID = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable = False)
    menus = db.relationship('menu', backref='employees')
    complaint = db.relationship('complaints', backref='employees')
    compliment = db.relationship('compliments', backref='employees')

    def __repr__(self):
        return "id: {0} | name: {1} | role: {2}".format(self.id, self.name, self.role)

class customers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(45), nullable = False)
    password = db.Column(db.String(255), nullable = False, unique = True)
    wallet = db.Column(db.Float(16,2), nullable = True, default = 0)
    isVIP = db.Column(db.Integer, nullable = True, default = 0)
    warning = db.Column(db.Integer, nullable = True, default = 0)
    isBlacklisted = db.Column(db.Integer, nullable = True, default = 0)
    AmountSpent = db.Column(db.Float(16,2), nullable = True, default = 0)
    rating = db.relationship('dishRating', backref='customers')
    order = db.relationship('orders', backref='customers')
    complain = db.relationship('complaints', backref='customers')
    compliment = db.relationship('compliments', backref='customers')
    #forgot isVIP in here. its TINYINT in MYSQL but you do db.Integer here

    def __repr__(self):
        return "id: {0} | name: {1} | password: {2}".format(self.id, self.name, self.password)

class menu(db.Model):
    id = db.Column(db.Integer,primary_key=True, nullable = False)
    chefID = db.Column(db.Integer,db.ForeignKey('employees.id'), nullable = False)
    businessID = db.Column(db.String(20), nullable = False)
    menudish = db.relationship('menuDishes', backref='menu')

    def __repr__(self):
        return "id: {0} | chef: {1} | business: {2}".format(self.id, self.chefID, self.businessID)

class dish(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name = db.Column(db.String(45), primary_key=True, nullable = False, unique = True)
    description = db.Column(db.String(255), nullable = False)
    bizID = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable = False)
    url = db.Column(db.String(255), nullable = False)
    menudish = db.relationship('menuDishes', backref='dish')
    rating = db.relationship('dishRating', backref='dish')
    orderline = db.relationship('orderLineItem', backref='dish')
    

    def __repr__(self):
        return "id: {0} | name: {1} | description: {2} | url: {3}".format(self.id, self.name, self.description, self.url)

        
#Likely requires ForeignKeyConstraint due to composite primary key made of foreign keys. Compiles for now.
class menuDishes(db.Model):
    __tablename__ = 'menuDishes'
    id = db.Column(db.Integer,db.ForeignKey('menu.id'),primary_key=True, nullable = False)
    MenuDishID = db.Column(db.Integer,db.ForeignKey('dish.id') ,primary_key=True, nullable = False)
    price = db.Column(db.Float, nullable = False)
    VIP = db.Column(db.Integer, nullable = False, default = 0)
    #__table_args__ = (db.ForeignKeyConstraint(id,MenuDishID))

class dishRating(db.Model):
    __tablename__ = 'dishRating'            #dumbest thing ever
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    rating = db.Column(db.Integer,  nullable = False)
    comment = db.Column(db.String(255), nullable = True)
    custID = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    dishID = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable = False)
    
class orders(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    total = db.Column(db.Float,  nullable = False)
    DeliveryTime = db.Column(db.String(45), nullable = True)
    Active = db.Column(db.Integer, nullable = False)
    custID = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    bizID = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable = False)
    orderline = db.relationship('orderLineItem', backref='orders')
    complaint = db.relationship('complaints', backref='orders')
    compliment = db.relationship('compliments', backref='orders')

class orderLineItem(db.Model):
    __tablename__ = 'orderLineItem'
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    quantity = db.Column(db.Integer,  nullable = False)
    subtotal = db.Column(db.Float,  nullable = False)
    discount = db.Column(db.String(45),  nullable = True)
    total = db.Column(db.Float,  nullable = False)
    orderID = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = False)
    DishOrdered = db.Column(db.Integer, db.ForeignKey('dish.id'),  nullable = False)

class complaints(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    comment = db.Column(db.String(255), nullable = False)
    complainer = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    complainee = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable = False)
    orderID = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = False)


class compliments(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    comment = db.Column(db.String(255), nullable = False)
    complimenter = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    complimentee = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable = False)
    orderID = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = False)
    


#Registration Authentication setup
class RegisterForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(
        min = 2, max = 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min = 2, max = 80)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    #Validating for existing usernames
    def validate_username(self, name):
        existing_user_name = customers.query.filter_by(
            name = name.data).first()
        if existing_user_name:
            raise ValidationError(
                "That username already exists, please choose another username")

#Login Authentication setup
class LoginForm(FlaskForm):
    name = StringField(validators=[InputRequired(), Length(
        min = 2, max = 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min = 2, max = 80)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

#######################################
###   Testing some functions

#
#def superuser(func):
#    @wraps(func)
#    def super_checker(*args, **kwargs):
#        if employees.name != 'Manager':
#            return redirect(url_for('login'))
#        return func(*args, **kwargs)
#    return super_checker
#
###@app.route('/employees/<Name>')
###@superuser
###@login_required
###def hire(Name):
###    form = RegisterForm()
###
###    if form.validate_on_submit():
###        hashed_password = bcrypt.generate_password_hash(form.password.data)
###        new_user = employees(name=form.name.data, password=hashed_password)
###        db.session.add(new_user)
###        db.session.commit()
###
###    return render_template('employee.html',form=form)
###    some form thingy for name of employee to hire.
###    adds that new user to the database and commmits. 




#this is the base routing "url" this is the standard home page
@app.route('/')
def home():
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
        
    is_employee = user_check()
    
    
    #the home function returns the home.html file
    return render_template('home.html', current_customer=current_customer, user=user, users_name=users_name, is_employee=is_employee)



#this is the routing for the login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    correct_creds = True
    blacklisted = False
    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')
        user = customers.query.filter_by(email=email).first()
        if user:
            if(user.isBlacklisted == 1):
                alert_user = "You do not have access to this site"
                blacklisted = True
                return render_template('login.html', alert_user = alert_user,blacklisted = blacklisted)
        if user:
            if(user.password == password):
                login_user(user)
                print("Logged in successfully!")
                counter = 0
                return redirect(url_for('customer_page'))
            else:
                # print("Incorrect credentials!")
                correct_creds = False
                alert_user = "You have entered the incorrect credentials. "
                return render_template('login.html', alert_user = alert_user, correct_creds = correct_creds)
        else:
            user = employees.query.filter_by(email=email).first()
            if user:
                if(user.password == password):
                    if (user.role == 'Chef'):
                        login_user(user)
                        print("Logged in successfully!")
                        return redirect(url_for('chef_page'))
                    if (user.role == 'Manager'):
                        login_user(user)
                        print("Logged in successfully!")
                        return redirect(url_for('manager_page'))
                    if (user.role == 'Delivery'):
                        login_user(user)
                        print("Logged in successfully!")
                        return redirect(url_for('delivery_page'))
                else:
                    correct_creds = False
                    alert_user = "You have entered the incorrect credentials. "
                    return render_template('login.html', alert_user = alert_user, correct_creds = correct_creds)
            else:
                print("No such username exists, try again")
    return render_template('login.html')    

def warn():
    userID = int(current_user.get_id())
    currUser = customers.query.filter_by(id = userID).first()
    if currUser.isVIP == 1 and currUser.warning >= 2:
        currUser.isVIP = 0
        currUser.warning = 0
        db.session.commit()
        print("VIP Status lost")
        return redirect(url_for('login'))
    elif currUser.warning >= 3:
        try:
            currUser.isBlacklisted = 1
            currUser.wallet = 0
            db.session.commit()
            logout_user()
            print("De-Registered")
            return True
        except:
            print("Deletion Failed")
    return None
    

def user_check():
    is_employee = 0
    if(current_user.is_authenticated):
        try:
            employee_check = int(current_user.get_id())
        except:
            print("You are not registered as an employee")
            return redirect(url_for('login'))
        print(current_user.get_id())
        if(employees.query.get(employee_check)):
            emp = employees.query.get(employee_check)
            if (emp.role == 'Manager'):
                is_employee = 1
            elif (emp.role == 'Chef'):
                is_employee = 2
            elif (emp.role == 'Delivery'):
                is_employee = 3
        else:
            is_employee = 4
    return is_employee
    #form = LoginForm()
    #This is what will happen when you press submit
    #if form.validate_on_submit():
        #it first checks for the username in the query of the database
        #user = customers.query.filter_by(name=form.name.data).first()
        #if username exists
       # if user:
            #checks if the passwords match
          #  if bcrypt.check_password_hash(user.password, form.password.data):
                #if passwords match, redirect to the dashboard page
              #  login_user(user)
              #  return redirect(url_for('dashboard'))
    #Login function returns the login.html file


#############################################################
#more app routes for menus, dishes, etc. 
#need to build templates for new routes. 

# These routes use index.html, to which you have to change the table according to the names in each class.
# I'm too lazy to bother making separate tables in html for each class even though
# its literally copy and paste with like two changes.

@app.route('/customers')
def index():
    all_customers = customers.query.all()
    return render_template('index.html', cust=all_customers)

# This uses jsonify to return more specific information from the database
# Doesnt work since jsonify cannot return queries. It usually returns lists/dictionaries.
# This means we would need to create our own serializer to fetch table data and convert into list/dicts. 
@app.route('/dish')
def dishes():
    all_dishes = dish.query.all()
    return render_template('index.html',dish=all_dishes)

# This route just prints the numbers, not the referenced items.
# 'menu' has a foreign key referencing employee.name, but employee.name isnt printed. (it works now) 
@app.route('/menu')
def menus():
    print(current_user.name)
    #all_dishes = menu.query.all()
    return render_template('menu.html')

#Completely untested Route.
@app.route('/VIPmenu', methods = ['GET', 'POST'])
def VIP():
    dished = dish.query.all()
    price = menuDishes.query.filter_by(VIP='1')
    lens = len(vip_tags)
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    try:
        user = int(current_user.get_id())
    except:
        print("You are not registered as a customer")
        return redirect(url_for('login'))
    print(current_user.get_id())
    if(employees.query.get(user)):
        pass
    if(customers.query.get(user)):
        cust = customers.query.get(user)
        if (cust.isVIP == 0):
            print(cust.name)
            print("You are not a VIP")
            return redirect(url_for('menu_popular'))
        
    is_employee = 0
    
    try:
        employee_check = int(current_user.get_id())
    except:
        print("You are not registered as an employee")
        return redirect(url_for('login'))
    print(current_user.get_id())
    if(employees.query.get(employee_check)):
        emp = employees.query.get(employee_check)
        if (emp.role == 'Manager'):
            is_employee = 1
        elif (emp.role == 'Chef'):
            is_employee = 2
        elif (emp.role == 'Delivery'):
            is_employee = 3
            
    if request.method == 'POST':
        try:
            user = int(current_user.get_id())
        except:
            print("You are not registered as a customer")
            return redirect(url_for('login'))
        
        if(customers.query.get(user) == None):
            print("you are not a customer, go buy somewhere else")
            return redirect(url_for('VIP'))
        
        quantity = request.form.get('quantity')
        dishes = request.form.get('dishid')
        cost = request.form.get('price')
        new_order = orders(custID=user, total=cost, bizID='1', Active='1')
        db.session.add(new_order)
        num = orders.query.order_by(orders.id.desc()).first()
        new_orderline = orderLineItem(quantity=quantity,subtotal=cost, DishOrdered=dishes,total=cost,orderID=num.id)
        db.session.add(new_orderline)
        db.session.commit()
        print("Added to cart")
        return redirect(url_for('VIP'))
    return render_template('VIPmenu.html',price=price,dish=dished, lens = lens, vip_tags=vip_tags, current_customer = current_customer, user=user, users_name=users_name, is_employee=is_employee)


#Currently not in use.
@app.route('/dishes')
def menudish():
    all_dishes = menuDishes.query.all()
    thing = dishRating.query.all()
    dished = dish.query.all()
    print(type(dished))
    dishing = dish.query.filter_by(name="Flaming Moe").first()
    order = orderLineItem.query.all()
    return render_template('index.html',order=order,thing=thing,dish = all_dishes, dished = dished, dishing = dishing)

@app.route('/dishes/popular') # im gonna completely ignore this route and not touch it and create a new one for popular dishes - Anthony
def popular():
    popular = dishRating.query.order_by(dishRating.rating.desc())
    return render_template('index.html',popular=popular)

#Currently not being used.
@app.route('/rating')
def dishlist():
    all_dishes = dishRating.query.all()
    return render_template('index.html',rating=all_dishes)
############################################################


#Currently not being used. 
@app.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

#Logout page
@app.route('/logout', methods = ['GET', 'POST'])
@login_required
def logout():
    
    logout_user()
    return redirect(url_for('login'))


#This is the routing for the registration page
@app.route('/register', methods = ['GET', 'POST'])
def register():
    #form = RegisterForm()
    if request.method =='POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        user = customers.query.filter_by(email=email).first()
        worker = employees.query.filter_by(email=email).first()
        #checks if email is already taken by customer or employee
        if user:
            print("Username already exists")
        if worker:
            print("Ay, im workin ova here!")
        else:
            new_user = customers(name=name, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            print("Thank you for registering!")
            return redirect(url_for('login'))
    #Hasing the password entered for encryption instead of being entered as plain-text
   # if form.validate_on_submit():
    #    hashed_password = bcrypt.generate_password_hash(form.password.data)
    #    new_user = customers(name=form.name.data, password=hashed_password)
    #    db.session.add(new_user)
        #db.session.commit()

    #returns the register.html file
    return render_template('register.html')#, '''form=form''')



@app.route('/menu_popular', methods = ['GET', 'POST'])
def menu_popular():
    #warn()
    user = 0
    users_name = ""
    dished = dish.query.all()
    price = menuDishes.query.all()
    ord = orderLineItem.query.all()
    lens = len(menu_tags)
    is_employee = user_check()
    randoms = [0, 1, 2]
        
    for i in randoms:
        randoms[i] = random.choice(price)
        print(randoms[i])
        while ((i>0) and (randoms[i] == randoms[i-1])):
            randoms[i] = random.choice(price)
        while ((i>1) and (randoms[i] == randoms[i-2])):
            randoms[i] = random.choice(price)
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
        #frequency = orders.query.filter_by(custID=user).all()
        #freq = len(frequency)
        #print(frequency)
        #print(freq)
        #if (freq < 3 ):
        #else: # check frequency of dishes ordered, top 3 displayed here
            #for i in randoms:
                #freq = len(frequency)
                #vari = random.randint(0,(freq-1))
                #randoms[i] = frequency[vari]
                #frequency.pop(vari)
                #while ((i>0) and (randoms[i] == randoms[i-1])):
                #    randoms[i] = random.choice(frequency)
                #    while ((i>1) and (randoms[i] == randoms[i-2])):
                #        randoms[i] = random.sample(frequency)
                #print(randoms[i].id)
    else: 
        current_customer = 0
    #ord = orderLineItem.query.filter_by(orderID=randoms[0].id).first()
    #print(ord.id)

    # This method below will handle the orders that come in from the menu. 
    # It needs to update two tables, "orders" and "orderLineItem".
    # Needs customerID, dishID, dish price, quantity of dish. 
    # Issue here is that "adding to cart" is being read as its own order. 
    if request.method == "POST":
        try:
            user = int(current_user.get_id())
        except:
            print("You are not registered as a customer")
            return redirect(url_for('login'))
        
        if(customers.query.get(user) == None):
            print("you are not a customer, go buy somewhere else")
            return redirect(url_for('menu_popular'))
        
        print(user)
        guy = customers.query.get(user)
        print(guy)
        quantity = request.form.get('quantity')
        dishes = request.form.get('dishid')
        cost = request.form.get('price')
        new_order = orders(custID=user, total=cost,Active='1', bizID='1')
        db.session.add(new_order)
        num = orders.query.order_by(orders.id.desc()).first()
        new_orderline = orderLineItem(quantity=quantity,subtotal=cost, DishOrdered=dishes,total=cost,orderID=num.id)
        db.session.add(new_orderline)
        db.session.commit()
        print("Added to cart")
        return redirect(url_for('menu_popular'))

    return render_template('menu_popular.html',rando=randoms,order=ord,price=price,dish=dished, lens = lens, menu_tags = menu_tags, current_customer = current_customer, user=user, users_name=users_name, is_employee=is_employee)

#adding money to wallet route
@app.route('/wallet', methods = ['GET', 'POST'])
@login_required
def wallet():
    user = 0
    users_name = ""
    alert_user = ""
    user_alert = ""
    is_employee = 0
    is_customer = True
    is_Valid = True
    try:
        employee_check = int(current_user.get_id())
    except:
        print("You are not registered as an employee")
        return redirect(url_for('login'))
    print(current_user.get_id())
    if(employees.query.get(employee_check)):
        emp = employees.query.get(employee_check)
        if (emp.role == 'Manager'):
            is_employee = 1
        elif (emp.role == 'Chef'):
            is_employee = 2
        elif (emp.role == 'Delivery'):
            is_employee = 3
    
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    if request.method == "POST":
        try:
            user = int(current_user.get_id())
        except:
            print("You are not registered as a customer")
            return redirect(url_for('login'))
        if(customers.query.get(user) == None):
            print("you are not a customer, go add balance somewhere else")
            is_customer = False
            alert_user = "You are not a customer. You cannot add balance."
            return redirect(url_for('wallet'))
            
        elif request.form.get('amount').isnumeric() == False or float(request.form.get('amount')) < 0:
            is_Valid = False
            user_alert = "Enter a valid amount"
            return render_template('wallet.html', user_alert = user_alert,is_Valid=is_Valid,is_customer=is_customer,user=user, users_name=users_name, current_customer=current_customer,is_employee=is_employee)
        else:
            amount = request.form.get('amount')
            userid = customers.query.filter_by(id = user).first()
            current_amount = float(userid.wallet)
            new_amount = current_amount + float(amount)
            userid.wallet = float(new_amount)
            db.session.commit()

    return render_template('wallet.html',alert_user=alert_user, is_customer=is_customer,user=user, users_name=users_name, current_customer=current_customer,is_employee=is_employee)

#Currently not in use
@app.route('/cart', methods = ['GET', 'POST'])
@login_required
def cart():
    user = 0
    users_name = ""
    is_employee = 0
    #
    #order.query.filter_by(Active='1')
    #
    alert_user = ""
    is_customer = True
    curr_user = int(current_user.get_id())
    in_cart = orders.query.filter_by(custID=curr_user,Active='1').all() #this is the selection query
    print(in_cart)
    items = orderLineItem.query.all()
    
    item_total = len(in_cart)
    subtotal = 0
    total_items = 0
    for c in in_cart:
        for i in items:
            if i.orderID == c.id:
                for q in range (0,i.quantity):
                    total_items += 1
                    subtotal = subtotal + c.total


    try:
        employee_check = int(current_user.get_id())
    except:
        print("You are not registered as an employee")
        return redirect(url_for('login'))
    print(current_user.get_id())
    if(employees.query.get(employee_check)):
        emp = employees.query.get(employee_check)
        if (emp.role == 'Manager'):
            is_employee = 1
        elif (emp.role == 'Chef'):
            is_employee = 2
        elif (emp.role == 'Delivery'):
            is_employee = 3
            
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
        if(customers.query.get(user) == None):
            print("you are not a customer, go add balance somewhere else")
            is_customer = False
            alert_user = "You are not a customer. You cannot add checkout or add balance."
            
    else: 
        current_customer = 0
    return render_template('cart.html',total_items=total_items,subtotal=subtotal,item_total=item_total,items=items,in_cart=in_cart,is_customer=is_customer,alert_user=alert_user, current_customer=current_customer, user=user, users_name=users_name, is_employee=is_employee)

@app.route('/checkout', methods = ['GET', 'POST'])
@login_required
def checkout():
    alert_user = ""
    is_Valid = True
    user = 0
    users_name = ""
    user_balance = float(current_user.wallet) #checks user balance
    enough_money = True
    subtotal = 0
    
    items = orderLineItem.query.all()
    
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    
    is_employee = 0
    
    try:
        employee_check = int(current_user.get_id())
    except:
        print("You are not registered as an employee")
        return redirect(url_for('login'))
        
    print(current_user.get_id())
    if(employees.query.get(employee_check)):
        emp = employees.query.get(employee_check)
        if (emp.role == 'Manager'):
            is_employee = 1
        elif (emp.role == 'Chef'):
            is_employee = 2
        elif (emp.role == 'Delivery'):
            is_employee = 3
    
    order = orders.query.filter_by(custID=user,Active='1').all()
    guy = customers.query.get(user)
    print(guy.wallet)
    for c in order:
        for i in items:
            if i.orderID == c.id:
                for q in range (0,i.quantity):
                    subtotal = subtotal + c.total
    if (user_balance < subtotal):
        enough_money = False;
        alert_user = "You do not have enough money to make this purchase. If you continue, you will get a warning."
        
    if request.method == 'POST':
        order = orders.query.filter_by(custID=user,Active='1').all()
        guy = customers.query.get(user)
        print(guy.wallet)
        ordxcc = len(order)
        subtotal = 0
        total_items = 0
        for c in order:
            for i in items:
                if i.orderID == c.id:
                    for q in range (0,i.quantity):
                        total_items += 1
                        subtotal = subtotal + c.total
        
        if(guy.wallet < float(subtotal)):
            guy.warning += float(1.0)
            db.session.commit()
            if (warn() == True):
                print("youre broke you poor lil shit")
                return redirect(url_for('login'))
            else:
                return redirect(url_for('checkout'))
        else:
            wallit = float(guy.wallet)
            moneytotal = wallit - float(subtotal)
            payup = float(guy.AmountSpent)
            broke = payup + float(subtotal)
            guy.wallet = moneytotal
            guy.AmountSpent = broke
            db.session.commit()
        print(type(order))
        print(len(order))
        if (len(order) == 0):
            is_Valid = False
            alert_user = "You do not have a valid amount of items in your cart"
            return render_template('checkout.html', user_balance=user_balance,user=user, users_name=users_name,current_customer=current_customer,is_employee=is_employee, is_Valid=is_Valid, alert_user=alert_user)
        else:
            print(order[0].Active)
            for i in range(0,ordxcc):
                order[i].Active = 0
                db.session.commit()
                print(order[i].Active)
            return redirect(url_for('customer_page'))
        
    return render_template('checkout.html', alert_user=alert_user,user_balance=user_balance,subtotal=subtotal,enough_money=enough_money,user=user, users_name=users_name,current_customer=current_customer,is_employee=is_employee)

@app.route('/customer_page', methods = ['GET', 'POST']) #customer page
@login_required
def customer_page():
    user = int(current_user.get_id())
    users_name = str(current_user.name)
    user_balance = float(current_user.wallet)
    vip_bool = 0
    try:
         (customers.query.get(user))
    except:
        return render_template('home.html')
    history = orders.query.filter_by(custID=user,Active='0')
    
    if(customers.query.get(user)):
        cust = customers.query.get(user)
        warnings = cust.warning
        if (cust.isVIP == 0):
            vip_bool = 0
        else:
            vip_bool = 1
    
    #print(history)
    items = orderLineItem.query.all()
    #Functionality for giving a customer VIP
    #query all the orderlineitem according to orderID which is specific to a user
    CustHistory = orders.query.filter_by(custID=user,Active='0').all()
    lenCust = len(CustHistory)
    total = 0

    custVIP = customers.query.filter_by(id = user).first()
    custVip = custVIP.isVIP
    guy = customers.query.get(user)
    
    #for o in CustHistory:
    #    total += float(o.total)
    custTotal = float(guy.AmountSpent)
    #check if they are VIP
    if lenCust >= 5 or custTotal >= 100:
        cust = customers.query.filter_by(id = user).first()
        if cust.isVIP == 0:
        #if they are not VIP, give them VIP
            cust.isVIP = 1
            db.session.commit()
            return render_template('customer_page.html')
 
   
    #item = orderLineItem.query.filter_by(orderID='1')
    #print(items[0])
    
    return render_template('customer_page.html',history=history,items=items, users_name = users_name, user=user,user_balance=user_balance, vip_bool=vip_bool,lenCust=lenCust, custTotal=custTotal,custVip=custVip,warnings = warnings)

@app.route('/delivery_page', methods = ['GET', 'POST']) #the delivery persons page
@login_required
def delivery_page():
    user2 = employees.query.filter_by(role="Delivery").first()
    print(current_user.name)
    print(user2.role)
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    try:
        print(current_user.role)
    except:
        print("You are not an employee!")
        return render_template('home.html')

    if (current_user.role != "Delivery"):
        print("You aren't a delivery boi")
        return render_template('home.html')
    return render_template('delivery_page.html', user=user,current_customer=current_customer,users_name=users_name)

@app.route('/manager_page_hire', methods = ['GET', 'POST'])
def manager_page_hire():
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    if request.method == "POST":
        if request.form.get('name') == '' or request.form.get('email') == '' or request.form.get('password') == '' or request.form.get('role') == '' or request.form.get('bizID') == '':
            print("Nothing Posted")
        else:
            name = request.form.get('name')
            email = request.form.get('email')
            password = request.form.get('password')
            role = request.form.get('role')
            bizID = request.form.get('bizID')
            new_employee = employees(name = name, email = email, password = password, role = role, bizID = bizID)
            db.session.add(new_employee)
            db.session.commit()
            print('Employee Added')
            return redirect(url_for('manager_page_hire'))

    return render_template('manager_page_hire.html', user=user,current_customer=current_customer, users_name=users_name)

@app.route('/manager_page_fire', methods = ['GET', 'POST'])
def manager_page_fire():
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    if request.method == "POST":
        if request.form.get('id') == '':
            print("Need a non empty ID")
        else:
            ids = request.form.get('id')
            try:
                employees.query.filter(employees.id == ids).delete()
                db.session.commit()
                print("Firing Successful")
                return redirect(url_for('manager_page_fire'))
            except:
                print("Firing Failed")

    return render_template('manager_page_fire.html',user=user, users_name=users_name, current_customer=current_customer)

@app.route('/manager_page', methods = ['GET', 'POST']) #the mananger's page
@login_required
def manager_page():
    # confirms the user accessing this page is the manager. Can be changed to filter by role="Manager" but too lazy.
    users = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        users = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
        
    user = employees.query.filter_by(id="1").first()
    if (current_user.get_id() != str(user.id)):
        print(current_user.get_id())
        print("You aren't the manager")
        return render_template('home.html')
    
    return render_template('manager_page.html', users_name=users_name,current_customer=current_customer,users=users)


@app.route('/chef_page_rm', methods = ['GET', 'POST']) #the chef's page remove function
def chef_page_rm():
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    dished = dish.query.all()
    if request.method == "POST":
        if request.form.get('id') == '':
            print("Need a non empty ID")
        else:
            ids = request.form.get('id')
            try:
                dish.query.filter(dish.id == ids).delete()
                db.session.commit()
                print("Deletion Successful")
                return redirect(url_for('chef_page_rm'))
            except:
                print("Deletion Failed")
    return render_template('chef_page_rm.html', dished = dished, user=user,current_customer=current_customer,users_name=users_name)


@app.route('/chef_page', methods = ['GET', 'POST']) #the chef's page
@login_required
def chef_page():
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    try:
        print(current_user.role)
    except:
        print("You are not an employee!")
        return render_template('home.html')

    if (current_user.role != "Chef"):
        print("You aren't a cook")
        return render_template('home.html')
    dished = dish.query.all()
    if request.method == "POST":
        if request.form.get('dish') == '' or request.form.get('description') == '' or request.form.get('bizID') == '' :
            print("Nothing Posted")
        else:
            dishes = request.form.get('dish')
            description = request.form.get('description')
            bizID = request.form.get('bizID')
            new_dish = dish(name = dishes, description = description, bizID = bizID)
            db.session.add(new_dish)
            db.session.commit()
            print("New Dish added")
            return redirect(url_for('chef_page'))

    return render_template('chef_page.html', dished = dished, user=user, users_name=users_name,current_customer=current_customer)

@app.route('/complaints', methods = ['GET','POST'])
@login_required
def complaint():
    user = int(current_user.get_id())
    if request.method == 'POST':
        comment = request.form.get('comment')
        victim = request.form.get('complainee')
        orderid = request.form.get('orderID')
        new_complaint = complaints(comment = comment, complainer = user, complainee = victim, orderID = orderid)
        db.session.add(new_complaint)
        db.session.commit()
    #return render_template('complaints.html')

@app.route('/compliments', methods = ['GET','POST'])
@login_required
def compliment():
    user = int(current_user.get_id())
    if request.method == 'POST':
        comment = request.form.get('comment')
        friend = request.form.get('complimenter')
        orderid = request.form.get('orderID')
        new_compliment = complaints(comment = comment, complainer = user, complainee = friend, orderID = orderid)
        db.session.add(new_compliment)
        db.session.commit()
    #return render_template('compliments.html')



@app.route('/contact_us', methods = ['GET', 'POST'])
def contact():
    user = 0
    users_name = ""
    if current_user.is_authenticated == True:
        current_customer = 1
        user = int(current_user.get_id())
        users_name = str(current_user.name)
    else: 
        current_customer = 0
    
    is_employee = 0
    
    if(current_user.is_authenticated):
        try:
            employee_check = int(current_user.get_id())
        except:
            print("You are not registered as an employee")
            return redirect(url_for('login'))
        print(current_user.get_id())
        if(employees.query.get(employee_check)):
            emp = employees.query.get(employee_check)
            if (emp.role == 'Manager'):
                is_employee = 1
            elif (emp.role == 'Chef'):
                is_employee = 2
            elif (emp.role == 'Delivery'):
                is_employee = 3
        else:
            is_employee = 4
    return render_template('contact_us.html', current_customer = current_customer, user=user, users_name=users_name ,is_employee=is_employee)

num = orderLineItem.query.filter_by(orderID = 3).first()
print(num.orderID)

if __name__ == '__main__':
    app.run(debug=True)
