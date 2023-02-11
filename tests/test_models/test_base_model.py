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
        self.assertTrue(hasattr(self.basemodel, "created_at"))
        self.assertIsInstance(self.basemodel.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at"""
        self.assertTrue(hasattr(self.basemodel, "updated_at"))
        self.assertIsInstance(self.basemodel.updated_at, datetime)

    @classmethod
    def tearDownClass(self):
        """Remove set up instance"""
        pass
if __name__ == "__main__":
    unittest.main()
