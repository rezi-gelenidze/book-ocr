import os

import config

# Separated responsibility modules
import optimizer, assembler, recognition


def main():
    raw_images = os.listdir(config.RAW_SOURCE_DIR)

    print("Optimizing images...")
    # Iterate over images in raw to optimize each
    for image in raw_images:
        image_path = os.path.join(config.RAW_SOURCE_DIR, image)
        optimized_image_path = os.path.join(config.OPTIMIZED_SOURCE_DIR, image)

        optimizer.optimize(image_path, optimized_image_path)

    print("Images optimized.")

    # Extract text from each optimized image
    print("Extracting text from images...")
    extracted_texts_per_page = []
    optimized_images = os.listdir(config.OPTIMIZED_SOURCE_DIR)

    for image in optimized_images:
        image_path = os.path.join(config.OPTIMIZED_SOURCE_DIR, image)
        extracted_text = recognition.recognize(image_path)

        extracted_texts_per_page.append(extracted_text)

    # Assemble the extracted texts into speficied type
    print("Assembling text as single file...")
    assembler.assemble(extracted_texts_per_page)


if __name__ == "__main__":
    main()
