import cv2
import numpy as np


def optimize(input_path: str, output_path: str):
    # Read the image
    img = cv2.imread(input_path, cv2.IMREAD_COLOR)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a stronger blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use adaptive thresholding to enhance text lines while minimizing noise
    thresh = cv2.adaptiveThreshold(
        blurred, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV, 15, 10
    )

    # Perform morphological operations to strengthen text lines
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    morphed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)

    # Remove small noise blobs by applying contour filtering
    contours, _ = cv2.findContours(morphed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros_like(morphed)
    for contour in contours:
        if cv2.contourArea(contour) > 50:  # Filter out small areas
            cv2.drawContours(mask, [contour], -1, 255, -1)

    # Apply the mask to the thresholded image
    cleaned = cv2.bitwise_and(morphed, mask)

    # invert the image
    cleaned = cv2.bitwise_not(cleaned)

    # Save the processed image
    cv2.imwrite(output_path, cleaned)

