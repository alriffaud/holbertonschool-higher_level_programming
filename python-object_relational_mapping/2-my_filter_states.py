#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=argv[1],
                            password=argv[2],
                            db=argv[3],
                            charset="utf8"
                            )
    cur = db.cursor()
    cur.execute("SELECT *\
                FROM states\
                WHERE name\
                LIKE BINARY '{}'\
                ORDER BY id ASC".format(argv[4]))
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
