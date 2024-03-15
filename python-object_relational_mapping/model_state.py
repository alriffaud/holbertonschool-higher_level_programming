#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base():
"""
from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/\
                {}'.format(username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
