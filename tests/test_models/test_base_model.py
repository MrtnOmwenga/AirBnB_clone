#!/usr/bin/env python3
"""
Test Base model class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Base Model"""
    @classmethod
    def setUpClass(self):
        """Set up instance for tests"""
        self.basemodel = BaseModel()

    def test_uuid(self):
        """Test uuid"""
        bm1 = self.basemodel
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm2.id, str)

    def test_created_at(self):
        """Test created_at"""
        new_d = datetime.now()
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertIsInstance(self.basemodel.created_at, datetime)
        self.assertNotEqual(self.basemodel.created_at.microsecond,
                         new_d.microsecond)

    def test_updated_at(self):
        """Test updated_at"""
        new_d = datetime.now()
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertIsInstance(self.basemodel.updated_at, datetime)
        self.assertNotEqual(self.basemodel.updated_at.microsecond,
                            new_d.microsecond)

    def test_to_dict(self):
        """Test to_dict() method"""
        self.basemodel.name = "Luffy"
        self.basemodel.friends = 9
        d = self.basemodel.to_dict()
        self.assertEqual(d["id"], self.basemodel.id)
        self.assertEqual(d["created_at"],
                         self.basemodel.created_at.isoformat())
        self.assertEqual(d["updated_at"],
                         self.basemodel.updated_at.isoformat())
        self.assertEqual(d["name"], self.basemodel.name)
        self.assertEqual(d["friends"], self.basemodel.friends)
        self.assertEqual(d["__class__"], type(self.basemodel).__name__)

    @classmethod
    def tearDownClass(self):
        """Remove set up instance"""
        pass
if __name__ == "__main__":
    unittest.main()
