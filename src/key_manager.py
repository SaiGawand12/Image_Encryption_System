import os
from cryptography.fernet import Fernet

class KeyManager:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        if not os.path.exists(self.key_file):
            self.generate_key()

    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        return open(self.key_file, 'rb').read()