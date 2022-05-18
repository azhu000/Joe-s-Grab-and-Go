# CSC322-SWE-Group-Project
Group project for CSC33200

To use your own local database, change the "conn" variable to your own information in this format:

conn = "mysql+pymysql://{0}:{1}@{2}/{3}" 

0 = the username of your DB

1 = the password of your DB

2 = the host/localhost of your DB (its usually localhost if you arent hosting it online)

3 = the name of your DB


Initial setup:
- install mysql (5.8+)
  -- run the init schema script 
- install python (3.9)
- pip install flask flask_sqlalchemy flask_login flask_bcrypt flask_wtf wtforms email_validator pip install mysql-connector-python
- pip install pymysql

- Run  flask_app.py
  
Developers:

- Anthony Zhu
- Anson Oommen,
- Pablo Lara,
- Ali Mohamed,
- Hyemin Shin
