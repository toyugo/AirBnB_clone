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
        return (self.__objects)

    def new(self, obj):
        """ new method """
        print("create new")
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """
        serializes __objects to the JSON
        """
        dico = {}
        for k in self.__objects:
            dico[k] = self.__objects[k].to_dict()
        with open(self.__file_path, mode="w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserialize the JSON v = dictionnary obj json """
        with open(self.__file_path) as f:
            json_file = json.load(f)
            for k, v in json_file.items():
                key = v["__class__"]
                self.new(eval(key)(**v))
