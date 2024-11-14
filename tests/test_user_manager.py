import unittest
from unittest.mock import patch, MagicMock
from src.user_manager import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.user_manager = UserManager()

    @patch('builtins.input', side_effect=['admin', 'password'])
    def test_authenticate_user_success(self, mock_input):
        self.assertTrue(self.user_manager.authenticate_user())
        self.assertEqual(self.user_manager.username, 'admin')

    @patch('builtins.input', side_effect=['admin', 'wrongpassword'])
    def test_authenticate_user_failure(self, mock_input):
        self.assertFalse(self.user_manager.authenticate_user())

    @patch('builtins.input', side_effect=['', 'password'])
    def test_authenticate_user_empty_username(self, mock_input):
        self.assertFalse(self.user_manager.authenticate_user())

    @patch('builtins.input', side_effect=['admin', ''])
    def test_authenticate_user_empty_password(self, mock_input):
        self.assertFalse(self.user_manager.authenticate_user())

if __name__ == '__main__':
    unittest.main()