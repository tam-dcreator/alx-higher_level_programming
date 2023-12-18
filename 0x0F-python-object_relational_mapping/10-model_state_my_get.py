#!/usr/bin/python3
"""
A Module that uses ORM and prints the state object with the name passed into it
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from sys import argv

    # Create a new engine for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a session using the engine
    session = Session(bind=engine)

    # Query the session, filter by state with the name passed in and print
    result = (session.query(State).filter_by(name='%s' % (argv[4],)).
              order_by(State.id).one_or_none())

    if result:
        print(result.id)
    else:
        print("Not found")
