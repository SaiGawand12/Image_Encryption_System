# tests/test_image_encryptor.py

import unittest
import os
from src.key_manager import KeyManager
from src.image_encryptor import ImageEncryptor

class TestImageEncryptor(unittest.TestCase):
    def setUp(self):
        self.key_manager = KeyManager('test_key.key')
        self.key = self.key_manager.load_key()
        self.image_encryptor = ImageEncryptor(self.key)
        self.test_image_path = 'test_image.jpg'
        self.encrypted_image_path = 'test_image_encrypted.enc'
        self.decrypted_image_path = 'test_image_decrypted.png'

        # Create a test image
        with open(self.test_image_path, 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\xf3\xff\xff\x00\x00\x00\x00IEND\xAEB`\x82')

    def test_encrypt_image(self):
        encrypted_path = self.image_encryptor.encrypt_image(self.test_image_path)
        self.assertTrue(os.path.exists(encrypted_path))

    def test_decrypt_image(self):
        self.image_encryptor.encrypt_image(self.test_image_path)
        decrypted_path = self.image_encryptor.decrypt_image(self.encrypted_image_path)
        self.assertTrue(os.path.exists(decrypted_path))

    def tearDown(self):
        os.remove(self.test_image_path)
        if os.path.exists(self.encrypted_image_path):
            os.remove(self.encrypted_image_path)
        if os.path.exists(self.decrypted_image_path):
            os.remove(self.decrypted_image_path)
        os.remove('test_key.key')

if __name__ == '__main__':
    unittest.main()