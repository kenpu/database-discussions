import sqlite3
from flask import Flask, request, render_template, abort, jsonify

app = Flask(__name__)


def connect():
    db = sqlite3.connect("./db.sqlite3")
    return db

def setup_db():
    db = connect()
    c = db.cursor()
    c.execute("""
        drop table if exists messages
    """)
    c.execute("""
        create table messages (name string, message string)
    """)
    db.commit()

def table_exists(t):
    db = connect()
    c = db.cursor()
    c.execute("select count(*) from sqlite_master where name = ?", [t])
    rows = c.fetchall()
    return rows[0][0] > 0

def get_column_names(t):
    db = connect()
    c = db.cursor()
    c.execute("select * from %s limit 1" % t)
    return [x[0] for x in c.description]

def question_marks(col_names):
    return ",".join("?" for x in col_names)

def insert_row(t, row):
    col_names = get_column_names(t)
    sql = "insert into %s values(%s)" % (t, question_marks(col_names))
    db = connect()
    c = db.cursor()
    c.execute(sql, [row.get(x) for x in col_names])
    db.commit()

def select_rows(t, data):
    sql = "select * from %s" % t
    db = connect()
    c = db.cursor()
    c.execute(sql)
    return c.fetchall()

@app.route('/')
def Index():
    return render_template("index.html")

@app.route("/debug")
def Debug():
    return "Result: %s, %s" % (table_exists("A"), table_exists("T"))

@app.route('/api/insert/<table>')
def Insert(table):
    if table_exists(table):
        row = request.args
        insert_row(table, row)
        return "ok"
    else:
        abort(500)

@app.route('/api/select/<table>')
def Select(table):
    if table_exists(table):
        rows = select_rows(table, request.args)
        return jsonify(rows)
    else:
        abort(500)

setup_db()
app.run(debug=True, port=4000)
