import sqlite3
import time
from random import random

def pause():
    time.sleep(random() * 1)

def setup():
    db = sqlite3.connect("shared.db")
    c = db.cursor()
    c.execute("create table if not exists T (value int)")
    c.execute("delete from T")
    c.execute("insert into T values (0)")
    db.commit()
    db.close()

def task1(n, transaction=False):
    db = sqlite3.connect("shared.db")
    c = db.cursor()
    for i in range(n):
        # get the smallest
        try:
            if transaction:
                c.execute("begin transaction")

            c.execute("select min(value) from T")
            smallest = c.fetchone()[0]

            pause()

            # get the largest
            c.execute("select max(value) from T")
            largest = c.fetchone()[0]

            if transaction:
                db.commit()

            if smallest <= largest:
                print "Consistent", i
            else:
                print "Inconsistency at %s, %d < %d" % (
                        i, smallest, largest)
        except:
            print "Busy at", i

def task2(n):
    db = sqlite3.connect("shared.db")
    c = db.cursor()
    for i in range(n):
        c.execute("begin transaction")
        sql = "update T set value = ?"
        value = -1 if i % 2 == 0 else 1
        c.execute(sql, [value])
        db.commit()
        pause()

if __name__ == '__main__':
    import sys
    from multiprocessing import Process
    transaction = sys.argv[1:]

    setup()
    N = 10
    p1 = Process(target=task1, args=(N,transaction))
    p2 = Process(target=task2, args=(N,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

