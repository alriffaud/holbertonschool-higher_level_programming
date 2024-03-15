#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    try:
        mysql_username = argv[1]
        mysql_password = argv[2]
        database_name = argv[3]
        db = MySQLdb.connect(
                                host="localhost",
                                port=3306,
                                user=mysql_username,
                                passwd=mysql_password,
                                db=database_name)
        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY id ASC")
        for row in cur.fetchall():
            print(row)
        cur.close()
        db.close()
    except Exception as e:
        print("ERROR: {}".format(e))
