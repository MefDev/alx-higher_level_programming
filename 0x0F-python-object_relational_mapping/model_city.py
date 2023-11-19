#!/usr/bin/python3
"""City class to table in database"""

from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """City table class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id))
