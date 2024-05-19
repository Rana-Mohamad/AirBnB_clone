#!/usr/bin/python3
''' File storage module. '''


import json
from models.base_model import BaseModel
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    ''' File Storage class. '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' Returns the dictionary __objects. '''

        return FileStorage.__objects

    def new(self, obj):
        ''' Sets in __objects the obj with key <obj class name>.id. '''

        obj_cls_name = obj.__class__.__name__

        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serializes __objects to the JSON file (path: __file_path). '''

        objs = FileStorage.__objects
        obj_dict = {}

        for obj in objs.keys():
            obj_dict[obj] = objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        '''
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        '''

        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        cls_name, obj_id = key.split('.')
                        cls = eval(cls_name)
                        instance = cls(**value)

                        FileStorage.__objects[key] = instance

                except Exception:
                    pass
