#from crypt import methods
#from ctypes import addressof
from functools import wraps
from unicodedata import name
import bcrypt
from click import password_option
from flask import Flask, redirect, render_template, url_for, request
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

# loads the user id which is stored
@login_manager.user_loader
def load_user(customers_id):
    return customers.query.get(int(customers_id))




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
    password = db.Column(db.String(255), nullable = False)
    role = db.Column(db.String(45), nullable = False)
    bizID = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable = False)
    menus = db.relationship('menu', backref='employees')

    def __repr__(self):
        return "id: {0} | name: {1} | role: {2}".format(self.id, self.name, self.role)

class customers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    name = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(255), nullable = False, unique = True)
    rating = db.relationship('dishRating', backref='customers')
    order = db.relationship('orders', backref='customers')

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
    menudish = db.relationship('menuDishes', backref='dish')
    rating = db.relationship('dishRating', backref='dish')
    orderline = db.relationship('orderLineItem', backref='dish')

    def __repr__(self):
        return "id: {0} | name: {1} | description: {2}".format(self.id, self.name, self.description)

        
#Likely requires ForeignKeyConstraint due to composite primary key made of foreign keys. Compiles for now.
class menuDishes(db.Model):
    __tablename__ = 'menuDishes'
    id = db.Column(db.Integer,db.ForeignKey('menu.id'),primary_key=True, nullable = False)
    MenuDishID = db.Column(db.Integer,db.ForeignKey('dish.id') ,primary_key=True, nullable = False)
    price = db.Column(db.String(20), nullable = False)
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
    total = db.Column(db.String(45),  nullable = False)
    DeliveryTime = db.Column(db.String(45), nullable = True)
    custID = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable = False)
    bizID = db.Column(db.Integer, db.ForeignKey('businesses.id'), nullable = False)
    orderline = db.relationship('orderLineItem', backref='orders')

class orderLineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable = False)
    quantity = db.Column(db.String(45),  nullable = False)
    subtotal = db.Column(db.String(45),  nullable = False)
    discount = db.Column(db.String(45),  nullable = True)
    total = db.Column(db.String(45),  nullable = False)
    orderID = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable = False)
    DishOrdered = db.Column(db.Integer, db.ForeignKey('dish.id'),  nullable = False)


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


def superuser(func):
    @wraps(func)
    def super_checker(*args, **kwargs):
        if employees.name != 'Manager':
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return super_checker

#######################################
###   Testing some functions

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
###    #some form thingy for name of employee to hire.
###    #adds that new user to the database and commmits. 
###
##
##
##@app.route('/employee_login', methods = ['GET', 'POST'])
##def login():
##    form = LoginForm()
##    #This is what will happen when you press submit
##    if form.validate_on_submit():
##        #it first checks for the username in the query of the database
##        user = employees.query.filter_by(name=form.name.data).first()
##        #if username exists
##        if user:
##            #checks if the passwords match
##            if bcrypt.check_password_hash(user.password, form.password.data):
##                #if passwords match, redirect to the dashboard page
##                login_user(user)
##                return redirect(url_for('employees'))
##    #Login fucntion returns the login.html file
##    return render_template('login.html', form=form)
##
## 


#this is the base routing "url" this is the standard home page
@app.route('/')
def home():
    #the home function returns the home.html file
    return render_template('home.html')

#this is the routing for the login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('email')
        password = request.form.get('password')
        user = customers.query.filter_by(name=name).first()
        if user:
            if(user.password == password):
                print("Logged in successfully!")
                return redirect(url_for('menus'))
            else:
                print("Incorrect credentials!")
        else:
            print("No such username exists, try again")

    
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
    #Login fucntion returns the login.html file
    return render_template('login.html')


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


@app.route('/dish')
def dishes():
    all_dishes = dish.query.all()
    return render_template('index.html',cust=all_dishes)

# This route just prints the numbers, not the referenced items.
# 'menu' has a foreign key referencing employee.name, but employee.name isnt printed. (it works now) 
@app.route('/menu')
def menus():
    #all_dishes = menu.query.all()
    return render_template('menu.html')

@app.route('/dishes')
def menudish():
    all_dishes = menuDishes.query.all()
    return render_template('index.html',dish=all_dishes)

@app.route('/dishes/popular') # im gonna completely ignore this route and not touch it and create a new one for popular dishes - Anthony
def popular():
    popular = dishRating.query.order_by(dishRating.rating.desc())
    return render_template('index.html',rating=popular)

@app.route('/rating')
def dishlist():
    all_dishes = dishRating.query.all()
    return render_template('index.html',rating=all_dishes)
############################################################




#upon successful login, this is the page that will be displayed
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
        name = request.form.get('email')
        password = request.form.get('password')

        user = customers.query.filter_by(name=name).first()
        if user:
            print("Username already exists")
        else:
            new_user = customers(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
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
    return render_template('menu_popular.html')

@app.route('/contact_us', methods = ['GET', 'POST'])
def contact():
    return render_template('contact_us.html')


if __name__ == '__main__':
    app.run(debug=True)