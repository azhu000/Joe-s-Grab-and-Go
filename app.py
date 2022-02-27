from flask import Flask, escape, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
   name = request.args.get("name", "World")
   return f'Hello, {escape(name)}!'

@app.route('/biz')
def biz():
    cnx = mysql.connector.connect(user='root', password='MyDBserver1998',
                                    host='localhost',
                                    database='test_schema')
    c = cnx.cursor()

    tablename = request.args.get("tablename", "businesses")
    print("Tablename is = ", tablename)

    c.execute(f'Select * from {tablename}')
    output = ""
    for row in c :
        output += "{}</br>".format(row)
    return output
