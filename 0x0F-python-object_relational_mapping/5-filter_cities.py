#!/usr/bin/python3
"""
A Module for listing cities from a database that are from a state that's passed
as an argument.
"""
if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    # No argument validation needed as per task requirement

    USERNAME = argv[1]
    PASSWORD = argv[2]
    DB_NAME = argv[3]
    STATE_NAME = argv[4]

    # Connect to Database

    conn = MySQLdb.connect(host="localhost", user=USERNAME, password=PASSWORD,
                           port=3306, database=DB_NAME)
    cur = conn.cursor()

    # Query Database and print result

    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name LIKE %s""", (STATE_NAME,))

    city_names = ", ".join(result[1] for result in cur.fetchall())

    print(city_names)

    # Close the connections

    cur.close()
    conn.close()
