#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

<<<<<<< HEAD
Base = declarative_base()

class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if models.storage_type == 'db':
=======
storage_type = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Representation of Amenity """
    if storage_type == 'db':
>>>>>>> 8f4da2bf40f7ad16af3606d9e68c62341d2b008e
        __tablename__ = 'amenities'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
