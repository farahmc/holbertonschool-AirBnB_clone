#!/usr/bin/python3
""" Unit tests for BaseModel """

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Unit tests for instantiating BaseModel """

    def test_instantiate(self):
        """ Happy pass instantiate"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """ Happy pass public id string format """
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """ Happy pass created at datetime """
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        """ Happy pass updated at datetime """
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uid(self):
        """ Test uid created at each instantiation """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)


if __name__ == "__main__":
    unittest.main()
