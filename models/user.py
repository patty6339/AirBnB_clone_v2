#!/usr/bin/python3
"""
This module defines a class User that inherits from BaseModel and Base
"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel):
    """This class defines a user by various attributes"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email = ''
        self.password = ''
    first_name = ''
    last_name = ''
