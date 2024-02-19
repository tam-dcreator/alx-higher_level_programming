#!/usr/bin/python3
"""
Script that takes a state name and list all the cities associated with it
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv as av

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=av[1], password=av[2], database=av[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM cities JOIN states ON
    cities.state_id = states.id WHERE BINARY states.name=%s ORDER BY
    cities.id ASC""", (av[4],))

    city_name = ", ".join(result[0] for result in cur.fetchall())
    print(city_name)

    cur.close()
    conn.close()
