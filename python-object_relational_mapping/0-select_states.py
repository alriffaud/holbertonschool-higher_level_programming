#!/usr/bin/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa.
"""


if __name__ == "__main__":
    import MySQLdb
    import sys
    from sys import argv
    try:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        db = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=mysql_username,
                                passwd=mysql_password,
                                db=database_name
                                )
        cur = db.cursor()
        cur.execute('SELECT * FROM states ORDER BY id ASC')
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
    except Exception:
        sys.exit(1)
