#!/usr/bin/python3
"""
A Module that contains a script that prints all city objects from a database
"""
if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import create_engine
    from sys import argv

    # Create a new engine for connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # Create a session using the engine
    session = Session(bind=engine)

    result = (session.query(State, City).filter(State.id == City.state_id)
              .order_by(City.id).all())

    for obj in result:
        obj_state = obj[0]
        obj_city = obj[1]
        print("{}: ({}) {}".format(obj_state.name, obj_city.id, obj_city.name))
