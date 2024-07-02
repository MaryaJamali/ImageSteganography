from PIL import Image
import numpy as np


def text_to_bits(text):
    """Convert text to bits."""
    # Convert text to binary and remove '0b' prefix
    bits = bin(int.from_bytes(text.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    # Pad with zeros to ensure the length of bits is a multiple of 8
    return bits.zfill(8 * ((len(bits) + 7) // 8))
