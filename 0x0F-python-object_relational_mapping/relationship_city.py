#!/usr/bin/python3
"""City class to table in database"""

from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base


class City(Base):
    """City table class"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
