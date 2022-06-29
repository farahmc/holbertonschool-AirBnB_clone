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

    def test_str_out(self):
        """ Happy pass string representation """
        base1 = BaseModel()
        str_out = f"[{base1.__class__.__name__}] ({base1.id} {base1.__dict__})"
        self.assertEqual(str_out, str(base1))

    def test_uid(self):
        """ UID created at each instantiation """
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_instantiate_attrs(self):
        """ Single instantiate and check attributes """
        base1 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime)
        self.assertEqual(type(base1.updated_at), datetime)

    def test_instantiate_kwargs(self):
        """ Single instantiate with kwargs """
        dt = datetime.today()
        base1 = BaseModel(
            id="123", created_at=dt.isoformat(), updated_at=dt.isoformat()
        )
        self.assertEqual(base1.id, "123")
        self.assertEqual(base1.created_at, dt)
        self.assertEqual(base1.updated_at, dt)

    def test_str(self):
        """ ___str__ method is string """
        base1 = BaseModel()
        self.assertEqual(type(str(base1)), str)


if __name__ == "__main__":
    unittest.main()
