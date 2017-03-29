import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def Hello():
    return "Hello"

@app.route("/name/<name>/age/<age>")
def Hello2(name, age):
    return "Name: %s, age: %s" % (name, age)

@app.route("/person")
def Hello3():
    return ",".join("%s=%s" % x for x in request.args.items())

app.run(debug=True, port=4000)
