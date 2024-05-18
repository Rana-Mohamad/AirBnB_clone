#!/usr/bin/python3
''' Module for amenity unittests. '''


import unittest
import os
import models
from datetime import datetime
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    ''' Unittest for Amenity class instantiation. '''

    def test_no_args_inst(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_inst_in_objs(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))
