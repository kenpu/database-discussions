import csv
import sqlite3
import sys
import os

def create_table(db, t, cols):
    cursor = db.cursor()

    tdef = ",".join("%s string" % x for x in cols)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS %s (%s);
    """ % (t, tdef))

def insert_row(db, t, row):
    n = len(row)
    placeholders = ",".join("?" for i in range(n))
    cursor = db.cursor()
    sql = "insert into %s values(%s)" % (t, placeholders)
    cursor.execute(sql, row)

if sys.argv[1:]:
    datafile = sys.argv[1]
else:
    print "Usage: %s <datafile>" % sys.argv[0]
    sys.exit(0)

db = sqlite3.connect("./build/database.sqlite3")
tablename = os.path.splitext(os.path.basename(datafile))[0]

with open(datafile) as f:
    reader = csv.reader(f)
    rows = list(reader)

columnnames = [unicode(x, errors="ignore") for x in rows[0]]

try:
    create_table(db, tablename, columnnames)
    for row in rows[1:]:
        insert_row(db, tablename, row)
    db.commit()
    print "Done"
except Exception, e:
    print e
