#!/usr/bin/python3
''' BaseModel class. '''

from datetime import datetime
import uuid
import models


class BaseModel:
    ''' BaseModel class. '''

    def __init__(self, *args, **kwargs):
        ''' Constructor. '''

        t_format = "%Y-%m-%dT%H:%M:%S.%f"

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if (key == "__class__"):
                    continue
                elif (key == "created_at" or key == "updated_at"):
                    setattr(self, key, datetime.strptime(value, t_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def save(self):
        ''' Updates the public instance attribute updated_at. '''

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of __dict__. '''

        dicts = self.__dict__.copy()
        dicts["__class__"] = self.__class__.__name__
        dicts["created_at"] = self.created_at.isoformat()
        dicts["updated_at"] = self.updated_at.isoformat()

        return dicts

    def __str__(self):
        ''' Returns a string. '''
        clsname = self.__class__.__name__

        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)
