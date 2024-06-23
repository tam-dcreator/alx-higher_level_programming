#!/usr/bin/python3
"""
A Module that contains a script that deletes all entries whose name has an 'a'
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from sys import argv

    # Create a new engine for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a session using the engine
    # Session = sessionmaker(bind=engine)
    session = Session(bind=engine)

    # Query the session to get obj, filter by 'a'
    to_delete = session.query(State).filter(State.name.like('%a%')).all()

    for obj in to_delete:
        session.delete(obj)
    session.commit()
