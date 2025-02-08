import os
import config

# Separated responsibility modules
import recognition, assembler


def main():
    # Extract text from each optimized image
    print("Extracting text from images..")
    pages = os.listdir(config.PAGES_SOURCE_DIR)

    # OCR recognize each page and append to the list (accumulator)
    extracted_texts_per_page = []
    for page_filename in pages:
        image_path = os.path.join(config.PAGES_SOURCE_DIR, page_filename)
        extracted_text = recognition.recognize(image_path)
        extracted_texts_per_page.append(
            (page_filename, extracted_text)
        )

    print("Text extracted from images.")

    # Save each page as a separate text file
    print("Assembling text as single file...")
    assembler.assemble(extracted_texts_per_page)

    print("Text assembled successfully.")

if __name__ == "__main__":
    main()
