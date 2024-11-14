# src/user_manager.py

import getpass

class UserManager:
    def __init__(self):
        self.users = {'admin': 'admin'}  

    def authenticate_user(self):
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        if username in self.users and self.users[username] == password:
            return True
        else:
            print("Invalid credentials.")
            return False