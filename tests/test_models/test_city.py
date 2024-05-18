#!/usr/bin/python3
''' Module for city unittest. '''


import unittest
import models
from models.city import City
from datetime import datetime


class TestCity_instantiation(unittest.TestCase):
    ''' Unittest for city instantiation. '''

    def test_no_arg(self):
        self.assertEqual(City, type(City()))

    def test_new_inst_in_objs(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_state_id_public_cls_atr(self):
        city = City()

        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_name_public_cls_atr(self):
        city = City()

        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_cities_unique_ids(self):
        city1 = City()
        city2 = City()

        self.assertNotEqual(city1.id, city2.id)
