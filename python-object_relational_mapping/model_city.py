#!/usr/bin/python3
"""
This module contain the City class.
"""
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    """
    City class to link to cities table in the database
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
