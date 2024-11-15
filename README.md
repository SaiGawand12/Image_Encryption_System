# Image Encryption System

This project provides an image encryption system that protects digital photos by transforming them into a coded format. It ensures that only authorized individuals can access or view the image content.

Click here to see [Live Demo](https://image-encryption-tool.streamlit.app/)

## Features

- Encryption algorithm selection (AES)
- Secure key management
- Real-time image encryption and decryption
- User authorization and access control
- Support for multiple image formats
- Integration of safe storage solutions

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SaiGawand12/image_encryption_system.git
   cd image_encryption_system
   ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
Run the application:
  ```bash
  python src/main.py
  ```

Follow the prompts to encrypt or decrypt images.

1. Login using username and password
2. press "e" to Encrypt, "d" to Decrypt an image, or "q" to quit.
3. Enter the path to the image file you want to encrypt or decrypt.
4. The encrypted or decrypted image will be saved in the same directory as the original image.


## Tests
To run the tests, navigate to the tests directory and run:
   ```bash
   python -m unittest discover
   ```

## Contributing
Contributions are welcome! If you have suggestions for improvements or features, feel free to fork the repository and submit a pull request.

## License
This project is licensed under the MIT [License](https://github.com/SaiGawand12/Image_Encryption_System/blob/main/LICENSE) - see the  file for details.

