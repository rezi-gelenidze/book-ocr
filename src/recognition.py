from pytesseract import image_to_string
from PIL import Image


def recognize(img_path: str) -> str:
    # Extract text from the image using Tesseract OCR
    return image_to_string(Image.open(img_path), lang='kat', config="--psm 6")

