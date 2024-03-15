#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa.
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=argv[1],
                            password=argv[2],
                            db=argv[3],
                            )
    cur = db.cursor()
    cur.execute("SELECT * FROM cities ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
