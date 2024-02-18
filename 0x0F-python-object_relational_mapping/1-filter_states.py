#!/usr/bin/python3
"""
Script that takes in a search parameter and displays all values that match it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv as av

    conn = MySQLdb.connect(host="localhost", port=3306, user=av[1],
                           password=av[2], database=av[3])
    cur = conn.cursor()

    cur.execute("""SELECT * FROM states WHERE name='{}' ORDER BY id ASC"""
                .format(av[4]))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    conn.close()
