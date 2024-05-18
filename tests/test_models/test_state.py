#!/usr/bin/python3
''' Module for state unittest. '''


import unittest
import models
from datetime import datetime
from models.state import State


class TestState_instantiation(unittest.TestCase):
    ''' Unittest for state instantiation. '''

    def test_no_arg(self):
        self.assertEqual(State, type(State()))

    def test_new_inst_in_objs(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_public_datetime(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_name_public_cls_atr(self):
        state = State()

        self.assertEqual(str, type(State.name))
        self.assertIn("name", dir(state))
        self.assertNotIn("name", state.__dict__)

    def test_two_states_unique_ids(self):
        state1 = State()
        state2 = State()

        self.assertNotEqual(state1.id, state2.id)
