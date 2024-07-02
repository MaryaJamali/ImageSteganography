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
