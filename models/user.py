#!/usr/bin/python3

<<<<<<< HEAD
=======
""" holds class User"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base

>>>>>>> 8f4da2bf40f7ad16af3606d9e68c62341d2b008e
"""
This module defines a class User that inherits from BaseModel and Base
"""


storage_type = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    """Representation of a user """
<<<<<<< HEAD
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
=======
    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship("Place", backref="user")
        reviews = relationship("Review", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
>>>>>>> 8f4da2bf40f7ad16af3606d9e68c62341d2b008e

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)
