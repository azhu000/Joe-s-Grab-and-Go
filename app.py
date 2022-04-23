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
#Uses SQLite3 as the test database, easy setup, just need to add the environment variables
#I already created a user, the username is: 'username' and the password is: 'test'
#Try it, see how it works, make your own user
#the site is localhost:5000/ for the homepage
#once you have sqlite3, you can see the users in the database by typing:
#'sqlite3 databse.db' in the terminal of vscode
#then typing 'select * from user'
#you should be able to see the username and the hashed password


#Creating the app which the Flsk app will run off
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
#Setting up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'secretkey'

#Login management
#loading users based on id's from the database
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

#loads the user id which is stored
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#setting up database ids
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable = False, unique = True)
    password = db.Column(db.String(20), nullable = False)

#Registration Authentication setup
class RegisterForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min = 4, max = 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min = 4, max = 20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    #Validating for existing usernames
    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username = username.data).first()
        if existing_user_username:
            raise ValidationError(
                "That username already exists, please choose another username")

#Login Authentication setup
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min = 4, max = 20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min = 4, max = 20)], render_kw={"placeholder": "Password"})
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
        user = User.query.filter_by(username=form.username.data).first()
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
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    #returns the register.html file
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
