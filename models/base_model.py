#!/usr/bin/python3
""" BaseModel class models.storage.new(self)"""
from datetime import datetime
import models
import uuid
import time


class BaseModel():
    """ Base Model """
    def __init__(self, *args, **kwargs):
        """ Init """
        form = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, form)
                else:
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # models.storage.new(self)

    def __str__(self):
        """ Print name and other info """
        nameClass = self.__class__.__name__
        idValue = self.id
        allAttribute = self.__dict__
        return "[{}] ({}) {}".format(nameClass, idValue, allAttribute)

    def save(self):
        """ Save """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dict = {}
        for i in self.__dict__:
            if i == "updated_at" or i == "created_at":
                dict[i] = getattr(self, i).isoformat()
            else:
                dict[i] = getattr(self, i)
        dict["__class__"] = self.__class__.__name__
        return dict
