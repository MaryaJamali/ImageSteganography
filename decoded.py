from PIL import Image
import numpy as np


def bits_to_text(bits):
    """Convert bits to text."""
    n = int(bits, 2)
    try:
        # Convert the integer to bytes and then to text
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'
    except UnicodeDecodeError:
        # Handle decoding errors
        return "Unable to decode message"


def decode_image(img_path):
    """Decode a message from an image."""
    img = Image.open(img_path)  # Open the image
    img = img.convert('RGB')  # Convert image to RGB format
    data = np.array(img)  # Convert image to numpy array

    # Extract bits from the image data
    flat_data = data.flatten()
    bits = [str(flat_data[i] & 1) for i in range(flat_data.size)]
    # Extract the least significant bit of each pixel
    bits = ''.join(bits)

    # Check if stopping byte is present
    stop_index = bits.find('00000000')
    if stop_index == -1:
        # If stopping byte is not found, the image is clean
        return "The image is clean"

    message_bits = bits[:stop_index]  # Find the bits of the message up to the stopping byte
    return bits_to_text(message_bits)  # Convert the bits to text


# This part extracts and prints the hidden message from the image "encoded_image.png".
decoded_message = decode_image('encoded_image.png')
print('Decoded message:', decoded_message)

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
