#!/usr/bin/python3
"""
A Module that uses ORM to list all objects from a database
"""
from model_state import Base, State
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

# Create a new engine for connection
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

# Bind it to the existing Base
Base.metadata.create_all(engine)

# Create a session using the engine
session = Session(bind=engine)

result = session.query(State).order_by(State.id).all()

for obj in result:
    print("%s: %s" % (obj.id, obj.name))
