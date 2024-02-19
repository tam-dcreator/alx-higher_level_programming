#!/usr/bin/python3
"""
A Module that uses ORM to list all State object that contains an 'a'
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

    # Query the session, filter by states that have 'a' in them and print
    result = (session.query(State).filter(State.name.like('%a%')).
              order_by(State.id).all())

    for obj in result:
        print(obj.id, obj.name, sep=": ")
