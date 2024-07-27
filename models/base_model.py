<<<<<<< HEAD

# #!/usr/bin/python3
# """
# Contains class BaseModel
# """

# from datetime import datetime
# import models
# from os import getenv
# import sqlalchemy
# from sqlalchemy import Column, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# import uuid

# time = "%Y-%m-%dT%H:%M:%S.%f"

# if models.storage_type == "db":
#     Base = declarative_base()
# else:
#     Base = object


# class BaseModel:
#     """The BaseModel class from which future classes will be derived"""
#     if models.storage_type == "db":
#         id = Column(String(60), primary_key=True)
#         created_at = Column(DateTime, default=datetime.utcnow)
#         updated_at = Column(DateTime, default=datetime.utcnow)

#     def __init__(self, *args, **kwargs):
#         """Initialization of the base model"""
#         if kwargs:
#             for key, value in kwargs.items():
#                 if key != "__class__":
#                     setattr(self, key, value)
#             if kwargs.get("created_at", None) and type(self.created_at) is str:
#                 self.created_at = datetime.strptime(kwargs["created_at"], time)
#             else:
#                 self.created_at = datetime.utcnow()
#             if kwargs.get("updated_at", None) and type(self.updated_at) is str:
#                 self.updated_at = datetime.strptime(kwargs["updated_at"], time)
#             else:
#                 self.updated_at = datetime.utcnow()
#             if kwargs.get("id", None) is None:
#                 self.id = str(uuid.uuid4())
#         else:
#             self.id = str(uuid.uuid4())
#             self.created_at = datetime.utcnow()
#             self.updated_at = self.created_at

#     def __str__(self):
#         """String representation of the BaseModel class"""
#         return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
#                                          self.__dict__)

#     def save(self):
#         """updates the attribute 'updated_at' with the current datetime"""
#         self.updated_at = datetime.utcnow()
#         models.storage.new(self)
#         models.storage.save()

#     def to_dict(self):
#         """returns a dictionary containing all keys/values of the instance"""
#         new_dict = self.__dict__.copy()
#         if "created_at" in new_dict:
#             new_dict["created_at"] = new_dict["created_at"].strftime(time)
#         if "updated_at" in new_dict:
#             new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
#         new_dict["__class__"] = self.__class__.__name__
#         if "_sa_instance_state" in new_dict:
#             del new_dict["_sa_instance_state"]
#         return new_dict

#     def delete(self):
#         """delete the current instance from the storage"""
#         models.storage.delete(self)

=======
>>>>>>> 8f4da2bf40f7ad16af3606d9e68c62341d2b008e
#!/usr/bin/python3
"""
Contains class BaseModel
"""

from datetime import datetime
import models
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

<<<<<<< HEAD
if models.storage_type == "db":
=======
storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
>>>>>>> 8f4da2bf40f7ad16af3606d9e68c62341d2b008e
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """The BaseModel class from which future classes will be derived"""
<<<<<<< HEAD
=======
    if storage_type == "db":
        id = Column(String(60), primary_key=True)
        created_at = Column(DateTime, default=datetime.utcnow)
        updated_at = Column(DateTime, default=datetime.utcnow)
>>>>>>> 8f4da2bf40f7ad16af3606d9e68c62341d2b008e

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.utcnow()
        for key, value in kwargs.items():
            if key == "created_at" and isinstance(value, str):
                value = datetime.strptime(value, time)
            elif key == "updated_at" and isinstance(value, str):
                value = datetime.strptime(value, time)
            if key != "__class__":
                setattr(self, key, value)

    def __str__(self):
        """String representation of the BaseModel class"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = {k: v.strftime(time) if isinstance(v, datetime) else v for k, v in self.__dict__.items()}
        new_dict["__class__"] = self.__class__.__name__
        new_dict.pop("_sa_instance_state", None)
        return new_dict

    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)