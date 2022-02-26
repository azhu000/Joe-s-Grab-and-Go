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

Developers: (Add your name here)

- Anthony Zhu
- Anson Oommen,
- Pablo Lara,
- Ali Mohamed,
- Hyemin Shin
