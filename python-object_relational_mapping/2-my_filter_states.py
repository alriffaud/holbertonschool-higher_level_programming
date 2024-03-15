#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

def main(argv):

    if len(argv) - 1 != 4:
        print("Must enter 4 arguments")
        return

    db = MySQLdb.connect(host="localhost",
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))

    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)

    db.close()


if __name__ == "__main__":
    import sys
    main(sys.argv)
