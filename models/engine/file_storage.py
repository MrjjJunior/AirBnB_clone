<<<<<<< HEAD
#!/bin/bash/python3

"""Defines a Filestorage class
"""

from models import *
import json
import os

class Filestorage():
    """Write a class FileStorage that serializes instances to a JSON file 
    and deserializes JSON file to instances
    attributes:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects
    """

    __file_path = "file.json"
    __objects = {}

    @publicmethod
    def all(self):
        """returns the dictionary __objects
        """
        return Filestorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key 
        """
        key = obj.__class__.__name__
        self.__objects["{}.{}".format(key, obj.id)] = obj

    def save(self):
        """serializes __objects to the JSON file
        """

        fd = {}
        
        for key, value in FileStorage.__objects.items():
            fd[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding='utf-8') as File:
            json.dump(fd, File, indent=4)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)
        """

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as File:
                my_dump = File.read()
        except FileNotFoundError:
            return

        objects = eval(my_dump)
        for (key, value) in objects.items():
            objects.key = "{} + '(**value)'".format(eval(key.split('.')[0]))
            self.__objects = objects
=======

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        obj_class_name = obj.__class__.__name__

        key = "{}.{}".format(obj_class_name, obj.id)

        FileStorage.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file  '''
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)

                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

>>>>>>> db0e851ee1e39b4ac3c0695415d5af10df97e9e9
