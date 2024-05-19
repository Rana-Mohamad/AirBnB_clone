#!/usr/bin/python3
''' Basemodel unittest module. '''


import unittest
from models.base_model import BaseModel


class TestBasemodel(unittest.TestCase):
    ''' Unittest for basemodel. '''

    def test_init(self):
        ''' Test for __init__. '''

        model = BaseModel()

        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)

    def test_save(self):
        ''' Test for save method. '''

        model = BaseModel()

        init_updated_at = model.updated_at
        cur_updated_at = model.save()

        self.assertNotEqual(init_updated_at, cur_updated_at)

    def test_to_dict(self):
        ''' Test for to_dict method. '''

        model = BaseModel()

        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)

        self.assertEqual(model_dict["__class__"], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())

    def test_str(self):
        ''' Test for __str__. '''

        model = BaseModel()

        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))


if __name__ == "__main__":
    unittest.main()
