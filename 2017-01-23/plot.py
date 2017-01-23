import sqlite3
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab
import math

db = sqlite3.connect('./build/database.sqlite3')
c = db.cursor()
c.execute("""
        WITH T(name, length) AS (
            SELECT rtrim(name, "EWNS"), Shape_Length FROM data
        )
        SELECT name, sum(length) as total
        FROM T
        group by name
        """)

rows = c.fetchall()

pylab.figure()
pylab.hist([float(x[1]) for x in rows], bins=100)
pylab.savefig('./build/lengths.png')

print "Done"
