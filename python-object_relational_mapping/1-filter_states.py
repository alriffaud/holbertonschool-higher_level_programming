#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    try:
        db = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY id ASC")
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print("ERROR: {}".format(e))
