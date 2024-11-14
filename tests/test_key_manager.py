# tests/test_key_manager.py

import unittest
import os
from src.key_manager import KeyManager

class TestKeyManager(unittest.TestCase):
    def setUp(self):
        self.key_manager = KeyManager('test_key.key')

    def test_key_generation(self):
        self.assertTrue(os.path.exists('test_key.key'))

    def test_load_key(self):
        key = self.key_manager.load_key()
        self.assertIsNotNone(key)

    def tearDown(self):
        os.remove('test_key.key')

if __name__ == '__main__':
    unittest.main()