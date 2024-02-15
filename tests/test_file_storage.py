#!/usr/bin/python
''' Unittest for file_storage '''

import models
import unittest
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    ''' Unittest for testing instantiation '''

    def test_FileStorage_no_args(self):
        ''' Test if there is no args '''
        self.assertEqual(type(FileStorage), FileStorage)

    def test_FileStorage_with_args(self):
        ''' Test if there is args '''
        with self.assertRaises(TypeError):
            FileStorage(None)
    
    def test_FileStorage_file_path_private_str(self):
        ''' Test if file path is a private string '''
        self.assertEqual(str, type (FileStorage._FileStorage__file_path))

    def test_FileStorage_object_is_private_dict(self):
        ''' Test if file object is private dict '''
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def tes_storage_initializes(self):
        self.assertEqual(type(models.staorage), FileStorage)