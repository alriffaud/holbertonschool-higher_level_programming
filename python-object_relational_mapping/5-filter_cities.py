#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
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
    cur.execute("SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id ASC", (argv[4],))
    if cur.fetchall():
        print(cur.fetchone()[0])
    cur.close()
    db.close()
