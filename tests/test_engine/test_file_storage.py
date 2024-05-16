#!/usr/bin/python3
''' FileStorage unittest module. '''


import unittest
import json
import models
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorage_inst(unittest.TestCase):
    ''' Unittest for FileStorage instantiation. '''

    def test_FileStorage_init_no_arg(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_init_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_methods(unittest.TestCase):
    ''' Unittesr for FileStorage methods. '''

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_model = BaseModel()
        models.storage.new(base_model)

        self.assertIn("BaseModel." + base_model.id, models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())

    def test_new_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        base_model = BaseModel()
        models.storage.new(base_model)
        models.storage.save()

        text = ""

        with open("file.json", "r", encoding="utf-8") as fi:
            text = fi.read()

            self.assertIn("BaseModel." + base_model.id, text)

    def test_save_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_model = BaseModel()
        models.storage.new(base_model)
        models.storage.save()
        models.storage.reload()

        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
