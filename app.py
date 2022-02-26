from flask import Flask, escape, request
import mysql.connector

app = Flask(__name__)

#@app.route('/')
#def hello():
#    name = request.args.get("name", "World")
#    return f'Hello, {escape(name)}!'

@app.route('/biz')
def biz():
    cnx = mysql.connector.connect(user='root', password='MyDBserver1998',
                                    host='localhost',
                                    database='test_schema')
    c = cnx.cursor()
    c.execute('Select * from businesses')
    output = ""
    for row in c :
        output += "{}".format(row)
    return output
    