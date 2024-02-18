#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv as av

    conn = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                           password=av[2], database=av[3])
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
