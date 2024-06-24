#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        try:
            from models import storage
            if not kwargs:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)
            else:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
                del kwargs['__class__']
                self.__dict__.update(kwargs)
        except Exception as e:
            print(f"Failed to initialize model: {e}")

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        try:
            from models import storage
            self.updated_at = datetime.now()
            storage.save()
        except Exception as e:
            print(f"Failed to save model: {e}")

    def __str__(self):
        """Returns a string representation of the instance with ordered keys"""
        cls = type(self).__name__
        return (
            '[{}] ({}) {{\'name\': \'{}\', \'created_at\': {}, '
            '\'id\': \'{}\'}}'.format(
                cls,
                self.id,
                self.name,
                repr(self.created_at),
                self.id
            )
        )

    # def save(self):
    #     """Updates updated_at with current time when instance is changed"""
    #     from models import storage
    #     self.updated_at = datetime.now()
    #     storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
