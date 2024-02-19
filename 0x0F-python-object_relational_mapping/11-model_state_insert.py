#!/usr/bin/python3
"""
A Module that contains a script that inserts a new row into the table object
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

    # Create a new state instance
    new_state = State(name="Louisiana")

    # Add to the session
    session.add(new_state)

    # Commit to DB
    session.commit()

    # Print the states.id of the new creation
    result = (session.query(State).filter_by(name='Louisiana').
              one_or_none())

    if result:
        print(result.id)
