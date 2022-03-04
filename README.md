# CSC322-SWE-Group-Project
Group project for CSC33200

Initial setup:
- install mysql (5.8+)
  -- run the init schema script 
- install python (3.9)
- install flask via pip: `pip install Flask`
- run the flask web server:

in order to activate the virtual environment... you have to be in the repository directory

and the use the command [ .\venv\Scripts\activate ] 

in order to deactivate the virtual environment, you can use the command [ deactivate ]

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

 ******** When running both the app.py and mysql_connect.py please make sure the correct credentials for the connection to the sql server. *********

Developers: (Add your name here)

- Anthony Zhu,
- Anson Oommen,
- Pablo Lara,
- Ali Mohamed,
- Hyemin Shin

