#!/usr/bin/python3
# Defines a state model
# INherits from mysqlalchemy base and links to the mysql tbale states

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Rrepresent a state for a mysql database

    __tablename__ (str) the name table for store states
    id (sqlalchemy.Integer): the states id
    name (sqlalchemy.String): the state's name
    """
    __tablename__ = "states"
    id = Column(String(128), nullable=False)
