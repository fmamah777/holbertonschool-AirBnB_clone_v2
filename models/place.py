#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
<<<<<<< HEAD
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
=======
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
from sqlalchemy.orm import relationship
from os import getenv
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
<<<<<<< HEAD
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
=======
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 back_populates='place_amenities',
                                 viewonly=False)
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096

    else:
        @property
        def reviews(self):
<<<<<<< HEAD
            """ Gets all reviews associated with Place """
            list_reviews = []
            for review in models.storage.all(Review).values:
                if self.id == review.place_id:
                    list_reviews.append(review)
            return list_reviews
=======
            """returns list of related reviews"""
            review_list = []
            for obj in models.storage.all(City).values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096

        @property
        def amenities(self):
            """ Gets all amenities associated with Place """
<<<<<<< HEAD
            list_amenities = []
            for amenity in models.storage.all("amenities").values:
                if self.id == amenity.place_id:
=======
            from models.amenity import Amenity
            from models import storage
            list_amenities = []
            for amenity in storage.all(Amenity).values():
                if amenity.id == self.amenity_id:
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
<<<<<<< HEAD
        def amenities(self, obj):
            """ Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_id """
            if type(obj) == 'Amenity':
                self.amenity_ids.append(obj.id)
=======
        def amenities(self, amenity_list):
            """ Setter attribute amenities that handles append method for
            adding an Amenity.id to the attribute amenity_id """
            from models.amenity import Amenity
            for obj in amenity_list:
                if type(obj) == Amenity:
                    self.amenity_ids.append(obj)
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
