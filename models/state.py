#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="State",
        cascade="all, delete, delete-orphan"
    )

    @property
    def cities(self): # +T6
        """Returns a list of City instances with state_id = id"""
        cities = []
        for thing in models.storage.all(City).values():
            if thing.state_id == self.id:
                cities.append(thing)
        return cities
