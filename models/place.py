#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)

    else:
        @property
        def reviews(self):
            """returns list of related reviews"""
            review_list = []
            for obj in models.storage.all(City).values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            """ Gets all amenities associated with Place """
            from models.amenity import Amenity
            from models import storage
            list_amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id == self.amenity_id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, amenity_list):
            """ Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_id """
            from models.amenity import Amenity
            for obj in amenity_list:
                if type(obj) == Amenity:
                    self.amenity_ids.append(obj)
