# CSC322-SWE-Group-Project
Group project for CSC33200
You shoud run this command in the terminal to download all the packages/modules:

pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator
pip install mysql-connector-python


To run this code, I have modified both login.html and register.html by changing form.username to form.name
This code requires you to install pymysql. 
pip install pymysql

To use your own local database, change the "conn" variable to your own information in this format:
conn = "mysql+pymysql://{0}:{1}@{2}/{3}" 
0 = the username of your DB
1 = the password of your DB
2 = the host/localhost of your DB (its usually localhost if you arent hosting it online)
3 = the name of your DB

# CSC322-SWE-Group-Project
Group project for CSC33200

Initial setup:
- install mysql (5.8+)
  -- run the init schema script 
- install python (3.9)
- install flask via pip: `pip install Flask`
- run the flask web server:
- ```bash
    set FLASK_APP=/full/path/to/your/folder/app.py
    python -m flask run
  ```
- Open your browser to the end points
  - `http://localhost:5000/`  
    - (return `Hello, World!`)
  - `http://localhost:5000/?name=JoeShmoe` 
    - (return `Hello, JoeShmoe`)
  - `http://localhost:5000/biz` 
    - (retuns contents of biz table `(1, "Moe's Tavern", '555 5th Avenue', '(212)-867-5309')`)
  - `http://127.0.0.1:5000/biz?tablename=dish` is an example. Replace `dish` with another table name. 

Developers: (Add your name here)

- Anthony Zhu
- Anson Oommen,
- Pablo Lara,
- Ali Mohamed,
- Hyemin Shin
