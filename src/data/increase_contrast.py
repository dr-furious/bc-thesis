import glob
import os

import cv2
import numpy as np


def power_law_transform(image: np.ndarray, gamma: float) -> np.ndarray:
    return np.array(255 * (image / 255) ** gamma, dtype="uint8")


def power_law_transform_all(image_dir: str, output_dir: str, gamma: float) -> None:
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all images in the specified folder (common formats)
    image_paths = glob.glob(os.path.join(image_dir, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png files
    for img_path in image_paths:
        image = cv2.imread(img_path)
        assert image is not None, "Image could not found"
        result = power_law_transform(image, gamma)

        # Extract filename and define output path
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)

        # Save the mask as a PNG file
        cv2.imwrite(output_path, result)
        print(f"Saved image to {output_path}")

