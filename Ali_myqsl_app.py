import bcrypt
from click import password_option
from flask import Flask, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LOGIN_MESSAGE, UserMixin, login_user, LoginManager, login_required, logout_user,current_user
from flask_wtf import FlaskForm
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


conn = "mysql+pymysql://root:MyDBserver1998@localhost/test_schema"

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

#loads the user id which is stored
@login_manager.user_loader
def load_user(customers_id):
    return customers.query.get(int(customers_id))

#setting up database ids
class customers(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(80), nullable = False, unique = True)

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


#this is the base routing "url" this is the standard home page
@app.route('/')
def home():
    #the home function returns the home.html file
    return render_template('home.html')

#this is the routing for the login page
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    #This is what will happen when you press submit
    if form.validate_on_submit():
        #it first checks for the username in the query of the database
        user = customers.query.filter_by(name=form.name.data).first()
        #if username exists
        if user:
            #checks if the passwords match
            if bcrypt.check_password_hash(user.password, form.password.data):
                #if passwords match, redirect to the dashboard page
                login_user(user)
                return redirect(url_for('dashboard'))
    #Login fucntion returns the login.html file
    return render_template('login.html', form=form)

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
    form = RegisterForm()

    #Hasing the password entered for encryption instead of being entered as plain-text
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = customers(name=form.name.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    #returns the register.html file
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)