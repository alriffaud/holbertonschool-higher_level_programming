#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
if __name__ == "__main__":
    import sys
    with MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3]) as db:
        db.execute("SELECT * FROM states ORDER BY id ASC")
        for row in db.fetchall():
            print(row)
