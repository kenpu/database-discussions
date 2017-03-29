import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def Hello3():
    return render_template("person.html", p=request.args)

app.run(debug=True, port=4000)
