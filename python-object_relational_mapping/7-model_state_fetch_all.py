#!/usr/bin/python3
"""
Write a script that lists all State objects from the database hbtn_0e_6_usa.
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                username, password, database), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(State.id)
    for row in states:
        print("{}: {}".format(row.id, row.name))
