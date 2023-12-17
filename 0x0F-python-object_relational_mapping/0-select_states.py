#!/usr/bin/python3
"""
A Module for listing states from a database
"""
if __name__ == "__main__":

    from sys import argv
    import MySQLdb

    # No argument validation needed as per task requirement

    USERNAME = argv[1]
    PASSWORD = argv[2]
    DB_NAME = argv[3]

    # Connect to Database

    conn = MySQLdb.connect(host="127.0.0.1", user=USERNAME, password=PASSWORD,
                           port=3306, database=DB_NAME)
    cur = conn.cursor()

    # Query Database and print result

    cur.execute("""SELECT * FROM states""")

    for result in cur.fetchall():
        print(result)

    # Close the connections

    cur.close()
    conn.close()
