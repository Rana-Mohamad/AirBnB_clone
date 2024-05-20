#!/usr/bin/python3
''' FileStorage unittest module. '''


import unittest
import json
import models
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_instantiation(unittest.TestCase):
    ''' Unittest for FileStorage instantiation. '''

    def test_FileStorage_inst_no_arg(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_inst_with_args(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_init(self):
        self.assertEqual(type(models.storage), FileStorage)

    def test_FileStorage_path_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objs_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))


class TestFileStorage_methods(unittest.TestCase):
    ''' Unittesr for FileStorage methods. '''

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base_model = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(place)
        models.storage.new(state)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)

        self.assertIn("BaseModel." + base_model.id,
                      models.storage.all().keys())
        self.assertIn(base_model, models.storage.all().values())

        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())

        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())

        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())

        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())

        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())

        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_new_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_save(self):
        base_model = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(place)
        models.storage.new(state)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()

        text = ""

        with open("file.json", "r", encoding="utf-8") as fi:
            text = fi.read()

            self.assertIn("BaseModel." + base_model.id, text)
            self.assertIn("User." + user.id, text)
            self.assertIn("Place." + place.id, text)
            self.assertIn("State." + state.id, text)
            self.assertIn("City." + city.id, text)
            self.assertIn("Amenity." + amenity.id, text)
            self.assertIn("Review." + review.id, text)

    def test_reload(self):
        base_model = BaseModel()
        user = User()
        place = Place()
        state = State()
        city = City()
        amenity = Amenity()
        review = Review()

        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(place)
        models.storage.new(state)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()

        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_model.id, objs)
        self.assertIn("User." + user.id, objs)
        self.assertIn("Place." + place.id, objs)
        self.assertIn("State." + state.id, objs)
        self.assertIn("City." + city.id, objs)
        self.assertIn("Amenity." + amenity.id, objs)
        self.assertIn("Review." + review.id, objs)

    def test_reload_with_args(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

        FileStorage._FileStorage__objects = {}


if __name__ == "__main__":
    unittest.main()
