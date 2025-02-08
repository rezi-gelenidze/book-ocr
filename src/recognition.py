import os

from pytesseract import image_to_string
from PIL import Image

from src import config


def recognize_pages() -> [str]:
    """
    Recognize text from each page and return a list of tuples containing the filename and the extracted text.
    :return:
    """
    print("Extracting text from images..")

    pages = os.listdir(config.PAGES_SOURCE_DIR)

    # OCR recognize each page and append to the list (accumulator)
    extracted_texts_per_page = []
    for page_filename in pages:
        image_path = os.path.join(config.PAGES_SOURCE_DIR, page_filename)

        extracted_text = image_to_string(
            Image.open(image_path), lang='kat', config="--psm 6"
        )

        extracted_texts_per_page.append(
            (page_filename, extracted_text)
        )

    print("Text extracted from images.")

    print("Saving extracted text to files..")
    for file_name, page_text in extracted_texts_per_page:
        # Save each page as a separate text file
        output_path = os.path.join(
            config.OCR_OUTPUT_DIR, f"{file_name.split('.')[0]}.txt"
        )

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(page_text)

    print("Extracted text .txt files saved to:", config.OCR_OUTPUT_DIR)
