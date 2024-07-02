from PIL import Image
import numpy as np


def text_to_bits(text):
    """Convert text to bits."""
    # Convert text to binary and remove '0b' prefix
    bits = bin(int.from_bytes(text.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    # Pad with zeros to ensure the length of bits is a multiple of 8
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def encode_image(img_path, message, output_path):
    """Encode a message into an image."""
    img = Image.open(img_path)  # Open the image
    img = img.convert('RGB')  # Convert image to RGB format
    data = np.array(img)  # Convert image to numpy array

    # Convert message to bits and add a stopping byte
    bits = text_to_bits(message) + '00000000'

    # Flatten the image data and embed the bits
    flat_data = data.flatten()
    for i in range(len(bits)):
        # Replace the least significant bit of each pixel with the message bit
        flat_data[i] = (flat_data[i] & ~1) | int(bits[i])

    # Reshape the data and save the new image
    new_data = flat_data.reshape(data.shape)
    # Convert the data array back to an image
    new_img = Image.fromarray(new_data.astype(np.uint8))
    new_img.save(output_path)


# This part hides the message in the image "input_image.png" and saves the result in "encoded_image.png".
encode_image('input_image.png',
             'Hello, my name is Maryam Jamali. I would be happy if you could tell me your opinion about my code in my email My email: m.jamali16@yahoo.com'
                      'encoded_image.png')

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
