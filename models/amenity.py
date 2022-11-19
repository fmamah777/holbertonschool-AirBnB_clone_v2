#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
<<<<<<< HEAD
from models.place import place_amenity
=======
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096


class Amenity(BaseModel, Base):
    """ This is the Amenity Class """
    from models.place import place_amenity
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
