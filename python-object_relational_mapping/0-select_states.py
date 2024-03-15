#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa.
"""
import MySQLdb
if __name__ == "__main__":
    import sys
    try:
        db = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=sys.argv[1],
                                password=sys.argv[2],
                                db=sys.argv[3]
                                )
    except MySQLdb.Error as error:
        sys.exit(1)
    cur = db.cursor()
    try:
        cur.execute('SELECT * FROM states ORDER BY id ASC')
        states = cur.fetchall()
        for row in states:
            print(row)
    except MySQLdb.Error as error:
        pass
    cur.close()
    db.close()
