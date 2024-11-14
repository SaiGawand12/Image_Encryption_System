from key_manager import KeyManager
from image_encryptor import ImageEncryptor
from user_manager import UserManager

def main():
    user_manager = UserManager()
    if not user_manager.authenticate_user():
        print("Authentication failed.")
        return

    key_manager = KeyManager()
    key = key_manager.load_key()
    if key is None:
        print("Failed to load key.")
        return

    image_encryptor = ImageEncryptor(key)

    while True:
        action = input("Do you want to (e)ncrypt, (d)ecrypt an image, or (q)uit? ").lower()
        if action == 'q':
            break

        image_path = input("Enter the image path: ")

        if action == 'e':
            try:
                encrypted_image_path = image_encryptor.encrypt_image(image_path)
                print(f"Image encrypted and saved as {encrypted_image_path}")
            except Exception as e:
                print(f"Error encrypting image: {str(e)}")
        elif action == 'd':
            try:
                decrypted_image_path = image_encryptor.decrypt_image(image_path)
                print(f"Image decrypted and saved as {decrypted_image_path}")
            except Exception as e:
                print(f"Error decrypting image: {str(e)}")
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()