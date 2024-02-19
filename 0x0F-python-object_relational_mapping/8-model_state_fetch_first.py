#!/usr/bin/python3
"""
A Module that uses ORM to print the first state object from a database
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

    # Query the session and print the result or 'Nothing' if no result
    result = session.query(State).order_by(State.id).first()

    if result:
        print(result.id, result.name, sep=": ")
    else:
        print("Nothing")
