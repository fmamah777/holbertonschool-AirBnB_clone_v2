#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
<<<<<<< HEAD
            return self.__objects
        return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
=======
            return FileStorage.__objects
        else:
            cls_objects = {}
            for value in FileStorage.__objects.values():
                if type(value) == cls:
                    cls_objects.update({value.to_dict()['__class__'] +
                                       '.' + value.id: value})
            return cls_objects
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r',) as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
<<<<<<< HEAD
        """ Deletes an object from memory """
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            try:
                del self.__objects[key]
            except KeyError:
                pass

    def close(self):
        """ Call reload() method for deserializing the json objects """
=======
        """Deletes obj if its inside"""
        if obj in self.__objects.values():
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects.pop(key, None)
        elif obj is None:
            return

    def close(self):
        """closes session"""
>>>>>>> ab8e3bc210730287e317579b1b978ff834094096
        self.reload()
