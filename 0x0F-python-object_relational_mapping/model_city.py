#!/usr/bin/python3
"""
A Module that creates a city definition of a City table
"""
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ A class definition for a city table with sqlalchemy
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))

    def __repr__(self):
        """ A default representation of this class
        """
        return "<City(name='%s')>" % self.name
