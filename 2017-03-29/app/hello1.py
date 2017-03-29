import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return "Hello"

app.run(debug=True, port=4000)
