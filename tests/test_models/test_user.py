#!/usr/bin/python3
''' Test user module. '''


import unittest
import os
import models
from datetime import datetime
from time import sleep
from models.user import User


class TestUser_instantiation(unittest.TestCase):
    ''' unit test for user instantiation. '''

    def test_no_args_inst(self):
        self.assertEqual(User, type(User()))

    def test_new_inst_in_objs(self):
        self.assertIn(User(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(User().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email_public_str(self):
        self.assertEqual(str, type(User.email))

    def test_password_public_str(self):
        self.assertEqual(str, type(User.password))

    def test_first_name_public_str(self):
        self.assertEqual(str, type(User.first_name))

    def test_last_name_public_str(self):
        self.assertEqual(str, type(User.last_name))

    def test_two_users_unique_id(self):
        f_user = User()
        s_user = User()

        self.assertNotEqual(f_user.id, s_user.id)
