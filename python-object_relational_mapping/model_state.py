#!/usr/bin/python3
'''
Module to create State model class
to be used as an Object mapper
'''


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class State(Base):
    '''
    State base model
    '''

    __tablename__ = "states"

    id = Column(Integer,
                autoincrement=True,
                nullable=False,
                unique=True,
                primary_key=True)

    name = Column(String(128),
                  nullable=False)
