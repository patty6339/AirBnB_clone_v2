#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            cascade="all, delete-orphan",
            backref="state"
        )
    else:
        @property
        def cities(self):
            """Getter attribute for cities that returns
                a list of City instances"""
            from models import storage
            city_list = []
            cities_dict = storage.all("City")
            for city in cities_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
