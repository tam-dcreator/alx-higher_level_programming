#!/usr/bin/python3
"""
Script that return names of states starting with N
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv as av

    conn = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                           password=av[2], database=av[3])
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id
    ASC""")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()
