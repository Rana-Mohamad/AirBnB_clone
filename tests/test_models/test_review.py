#!/usr/bin/python3
''' Module for review unittest. '''


import unittest
import models
from datetime import datetime
from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    ''' Unittest for review instantiation. '''

    def test_no_arg(self):
        self.assertEqual(Review, type(Review()))

    def test_new_inst_in_objs(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(Review().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(Review().updated_at))

    def test_place_id_public_cls_atr(self):
        review = Review()

        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(review))
        self.assertNotIn("place_id", review.__dict__)

    def test_user_id_public_cls_atr(self):
        review = Review()

        self.assertEqual(str, type(Review.user_id))
        self.assertIn("user_id", dir(review))
        self.assertNotIn("user_id", review.__dict__)

    def test_text_public_cls_atr(self):
        review = Review()

        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(review))
        self.assertNotIn("text", reveiw.__dict__)

    def test_two_reviews_unique_ids(self):
        review1 = Review()
        review2 = Review()

        self.assertNotEqual(review1.id, review2.id)
