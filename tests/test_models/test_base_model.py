#!/usr/bin/python3
''' Basemodel unittest module. '''


import unittest
from models.base_model import BaseModel
from datetime import datetime
import models


class TestBaseModel(unittest.TestCase):
    ''' Unittest for basemodel. '''

    def test_no_arg_inst(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_inst_in_obj(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        model1 = BaseModel()
        model2 = BaseModel()

        self.assertNotEqual(model1.id, model2.id)

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

        self.assertEqual(model_dict['__class__'], 'BaseModel')
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
