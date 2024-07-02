# ImageSteganography 🌁
## Description
This project provides a simple implementation of image steganography using Python. It allows you to hide a text message within an image and then extract it later.
## Features
- Encode a message into an image:** Hide a secret message inside an image.
- Decode a message from an image:** Extract the hidden message from an image.
## Requirements
- Python 3.x
- Required libraries:
  - `Pillow`
  - `numpy`
<br>⭐ You can install the required libraries using pip : ```pip install numpy Pillow```
## Installation
1. Clone the repository : ``` git clone https://github.com/MaryaJamali/ImageSteganography.git```
2. Move to the project directory : ```cd ImageSteganography```
3. Install the required packages : ```pip install -r requirements.txt```
4. Run the program
## Using the application
### 🌟 Encoding a Message
To encode a message into an image, use the encode_image.py script. This script will take an input image, a message, and an output image path to save the encoded image.
```python
encode_image('input_image.png',
             'Hello, my name is Maryam Jamali. I would be happy if you could tell me your opinion about my code in my email My email: m.jamali16@yahoo.com',
             'encoded_image.png')
```
### 🌟 Decoding a Message
To decode a message from an image, use the decode_image.py script. This script will take an input image path and return the hidden message if present.
```python
decoded_message = decode_image('encoded_image.png')
print('Decoded message:', decoded_message)
```
## Files
🔶 encode.py : This Python file contains codes related to encoding.<br>
🔶 decode.py : This Python file contains codes related to decoding.<br>
🔶 requirements.txt : List of required Python packages.<br>
## Contributing
Dear contributor are welcome! Please feel free to submit a pull request 💌 or open an issue 📩 if you have any suggestions or improvements.
## Author
Maryam Jamali 🤍
