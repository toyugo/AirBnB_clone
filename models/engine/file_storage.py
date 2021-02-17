#!/usr/bin/python3
""" FileStorage class """
import json
from os import path
from models.base_model import BaseModel


class FileStorage():
    """ File storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ all method """
        return (FileStorage.__objects)

    def new(self, obj):
        """ new method """
        print("create new")
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """Serialize __objects to  JSON ."""
        pass

    def reload(self):
        """Deserialize the JSON """
        pass
