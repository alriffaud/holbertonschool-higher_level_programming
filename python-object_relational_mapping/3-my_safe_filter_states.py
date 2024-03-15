#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time, write
one that is safe from MySQL injections
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
    cur.execute("SELECT * FROM states WHERE name = %s\
                ORDER BY id ASC", (argv[4],))
    for row in cur.fetchall():
        if row[1] == argv[4]:
            print(row)
    cur.close()
    db.close()
