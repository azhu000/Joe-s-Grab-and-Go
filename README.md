# CSC322-SWE-Group-Project
Group project for CSC33200
This template uses MySQL as the database.
You shoud run this command in the terminal to download all the packages/modules:
pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator

If you are having issues with sql:
So save the python codes, try running it, if it works great, or else this is what I did to initialize the data base with the users table:
1. First, you need to type 'python' or 'python3' (mac)
2. Then 'from app import db'
3. Then 'db.create_all()'
4. Then exit out python using 'exit()'
5. Then type 'sqlite3 database.db'
6. Then '.tables'
And if everything is correct, it should output users which means it recognized the users table we created
7. type '.quit' to exit out of sqlite3 command line

You can view the database query by typing 'sqlite3 database.db' and then 'select * from user;'
