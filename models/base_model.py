#!/usr/bin/python
"""Defining the base model class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the base model for the whole  AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new base model
        using: *args for unknown number of arguments passed
        using: **kwargs for key/value pairs of attributes
        """

        self.id = str(uuid4())
        time_form = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Will update the updtaed_at met with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Will return the dictiionary of the base model instance
        with key/value pairs with name of class as object
        """

        rDict = self.__dict__.copy()
        rDict["created_at"] = self.created_at.isoformat()
        rDict["updated_at"] = self.updated_at.isoformat()
        rDict["__class__"] = self.__class__.__name__
        return rDict

    def __str__(self):
        """Will return the print/str representation of the BaseModel 
        instance."""

        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)




