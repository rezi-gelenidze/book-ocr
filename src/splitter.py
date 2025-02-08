import os
import cv2

from src import config


def split_pairs():
    pairs = os.listdir(config.PAIRS_SOURCE_DIR)

    for pair_filename in pairs:
        img = cv2.imread(pair_filename)

        if img is None:
            raise FileNotFoundError(f"Image '{pair_filename}' not found.")

        # Get the height and width of the image
        _, w = img.shape

        # Split the image in half
        left_side = img[:, :w // 2]
        right_side = img[:, w // 2:]

        # Get the base name of the file (without extension)
        base_name, ext = os.path.splitext(pair_filename)

        left_path = os.path.join(config.PAGES_SOURCE_DIR, f"{base_name}_l{ext}")
        right_path = os.path.join(config.PAGES_SOURCE_DIR, f"{base_name}_r{ext}")

        # Save the left and right halves
        cv2.imwrite(left_path, left_side)
        cv2.imwrite(right_path, right_side)


if __name__ == "__main__":
    split_pairs()
