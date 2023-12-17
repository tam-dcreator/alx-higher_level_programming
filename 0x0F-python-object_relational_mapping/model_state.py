#!/usr/bin/python3
"""
A Module that creates a class definition of a State table
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a base for our table to inherit from
Base = declarative_base()


class State(Base):
    """ A class definition for a table with sqlalchemy
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        """ A default representation of this class
        """
        return "<State(name='%s')>" % self.name
