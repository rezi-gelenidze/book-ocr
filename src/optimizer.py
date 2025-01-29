import cv2
import numpy as np

def optimize(input_path: str, output_path: str):
    # Read the image
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Normalize the brightness and contrast to enhance text visibility
    cleaned = cv2.normalize(gray, None, 0, 255, cv2.NORM_MINMAX)

    # Save the processed image
    cv2.imwrite(output_path, cleaned)
