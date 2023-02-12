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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects, the obj with key <obj class name>.id"""
        FileStorage.__objects["{}.{}".format(
            type(obj).__name__, obj.id)] = obj

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

        classes = {"BaseModel": BaseModel}
        return classes

    def reload(self):
        """Deserializes JSON file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode="r",
                      encoding="utf-8") as f:
                data = json.load(f)
                d = {}
                for key, value in data.items():
                    c_name = value['__class__']
                    d[key] = self.classes()[c_name](**value)
                FileStorage.__objects = d
