#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base():
"""
import sys
from sqlalchemy import create_engine
from model_state import Base

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/\
                {}'.format(username, password, database), pool_pre_ping=True)
    Base.metadata.create_all(engine)
