#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from os import getenv


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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship("Amenity", secondary="place_amenity",
                                backref="place_amenities",
                                viewonly=False)
    else:
        @property
        def reviews(self):
            """Attribute for FileStorage"""
            review_list = []
            for el in models.storage.all(Review).values():
                if el.place_id == self.id:
                    review_list.append(el)
            # return review_list

        @property
        def amenities(self):
            """Returns a list of Amenities"""
            all_amenities = models.storage.all(Amenity)
            amenities = [amen for amen in all_amenities.values()
                         if amen.id == self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """Sets amenities into amenity_ids[]"""
            if isinstance(value, Amenity):
                amenity_ids.append(value.id)
