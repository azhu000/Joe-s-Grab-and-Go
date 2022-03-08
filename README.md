# Pablo Front End Notes
To access the material. Please follow the instructions below until a better method can be found.

1. Open up visual studio code, and go to the Extensions menu on the left hand bar.
2. Look up "Live Server." It is the first extension.
3. Install "Live Server"
4. Open up an html file on VS Code.
5. Right click and press Open with Live Server.

Once you press open with live server, it will open up a local host server on your web browser. Everytime you save the file, it should update as well. 

If it doesn't either refresh the page or do the following.

1. Go to the HTML file you're trying to see.
2. Right click and press Stop Live Server.
3. Then, right click, and press Open with Live Server again.

This should reset the page with your new version of the file. Thank you.


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

To run mysql_connect.py you need to install `mysql-connector-python`



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

- Anthony Zhu
- Anson Oommen,
- Pablo Lara,
- Ali Mohamed,
- Hyemin Shin

