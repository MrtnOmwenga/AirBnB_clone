#!/usr/bin/env python3
"""
Moduel Serializes and deserializes JSON
"""

import json
import os


class FileStorage():
    """This class serializes instances to JSON and vice versa"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects, the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(FileStorage.__file_path, mode="w",
                  encoding="utf-8") as f:
            d = {key: value.to_dict() for
                 key, value in FileStorage.__objects.items()}
            json.dump(d, f)

    def classes(self):
        """Return classess dictionary"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "State": State,
                   "City": City,
                   "Amenity": Amenity,
                   "Place": Place,
                   "Review": Review}
        return classes

    def reload(self):
        """Deserializes JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass
