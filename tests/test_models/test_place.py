#!/usr/bin/python3
''' Module for place unittest. '''


import unittest
import models
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    ''' Unittest for Place instantiation. '''

    def test_no_arg(self):
        self.assertEqual(Place, type(Place()))

    def test_new_inst_in_objs(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_city_id_public_cls_atr(self):
        place = Place()

        self.assertEqual(str, type(Place.city_id))
        self.assertIn("city_id", dir(place))
        self.assertNotIn("city_id", place.__dict__)

    def test_user_id_public_cls_atr(self):
        place = Place()

        self.assertEqual(str, type(Place.user_id))
        self.assertIn("user_id", dir(place))
        self.assertNotIn("user_id", place.__dict__)

    def test_name_public_cls_atr(self):
        place = Place()

        self.assertEqual(str, type(Place.name))
        self.assertIn("name", dir(place))
        self.assertNotIn("name", place.__dict__)

    def test_description_public_cls_atr(self):
        place = Place()

        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("description", place.__dict__)

    def test_number_rooms_public_cls_atr(self):
        place = Place()

        self.assertEqual(int, type(Place.number_rooms))
        self.assertIn("number_rooms", dir(place))
        self.assertNotIn("number_rooms", place.__dict__)

    def test_number_bathrooms_public_cls_atr(self):
        place = Place()

        self.assertEqual(int, type(Place.number_bathrooms))
        self.assertIn("number_bathrooms", dir(place))
        self.assertNotIn("number_bathrooms", place.__dict__)

    def test_max_guest_public_cls_atr(self):
        place = Place()

        self.assertEqual(int, type(Place.max_guest))
        self.assertIn("max_guest", dir(place))
        self.assertNotIn("max_guest", place.__dict__)

    def test_price_by_night_public_cls_atr(self):
        place = Place()

        self.assertEqual(int, type(Place.price_by_night))
        self.assertIn("price_by_night", dir(place))
        self.assertNotIn("price_by_night", place.__dict__)

    def test_latitude_public_cls_atr(self):
        place = Place()

        self.assertEqual(float, type(Place.latitude))
        self.assertIn("latitude", dir(place))
        self.assertNotIn("latitude", place.__dict__)

    def test_longitude_public_cls_atr(self):
        place = Place()

        self.assertEqual(float, type(Place.longitude))
        self.assertIn("longitude", dir(place))
        self.assertNotIn("longitude", place.__dict__)

    def test_amenity_ids_public_cls_atr(self):
        place = Place()

        self.assertEqual(list, type(Place.amenity_ids))
        self.assertIn("amenity_ids", dir(place))
        self.assertNotIn("amenity_ids", place.__dict__)

    def test_two_places_unique_id(self):
        place1 = Place()
        place2 = Place()

        self.assertNotEqual(place1.id, place2.id)
