#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
<<<<<<< HEAD
    """ class to store review information """
   
=======
    """ Review classto store review information """

>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
    __tablename__ = "reviews"
    text = Column(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
