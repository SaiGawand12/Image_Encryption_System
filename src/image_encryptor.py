# src/image_encryptor.py

from PIL import Image
import io
from cryptography.fernet import Fernet

class ImageEncryptor:
    def __init__(self, key):
        self.fernet = Fernet(key)

    def encrypt_image(self, image_path):
        with open(image_path, 'rb') as image_file:
            image_data = image_file.read()

        encrypted_data = self.fernet.encrypt(image_data)
        encrypted_image_path = image_path.split('.')[0] + "_encrypted.enc"

        with open(encrypted_image_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        return encrypted_image_path

    def decrypt_image(self, encrypted_image_path):
        with open(encrypted_image_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        decrypted_data = self.fernet.decrypt(encrypted_data)
        decrypted_image_path = encrypted_image_path.split('.')[0] + "_decrypted.png"

        with open(decrypted_image_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        return decrypted_image_path