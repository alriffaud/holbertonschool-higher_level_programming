#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=sys.argv[1],
                            password=sys.argv[2],
                            db=sys.argv[3]
                            )
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE %s ORDER BY id',
                (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
