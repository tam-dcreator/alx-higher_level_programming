#!/usr/bin/python3
"""
A Module that contains a script that changed the name of a state object
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

    # Query the session to get obj, filter by id
    to_change = (session.query(State).filter_by(id=2).one_or_none())

    if to_change:
        to_change.name = "New Mexico"

        # Add to session and commit
        session.add(to_change)
        session.commit()
