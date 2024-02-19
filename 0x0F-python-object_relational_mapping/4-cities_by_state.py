#!/usr/bin/python3
"""
Script that list cities from a database
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as av

    conn = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                           password=av[2], database=av[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM cities ORDER BY cities.id ASC""")

    for result in cur.fetchall():
        print(result)
    cur.close()
    conn.close()
