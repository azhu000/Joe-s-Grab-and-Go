# CSC322-SWE-Group-Project
Group project for CSC33200
You shoud run this command in the terminal to download all the packages/modules:
pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
pip install mysql-connector-python


To run this code, i have modified both login.html and register.html by changing form.username to form.name
This code requires you to install pymysql. 
pip install pymysql
It is a modified version of anson's code, capable of running with MySQL.
To use your own local database, change the "conn" variable to your own information in this format:
conn = "mysql+pymysql://{0}:{1}@{2}/{3}" 
0 = the username of your DB
1 = the password of your DB
2 = the host/localhost of your DB (its usually localhost if you arent hosting it online)
3 = the name of your DB

