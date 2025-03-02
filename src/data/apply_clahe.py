import glob
import os
from typing import Tuple
import numpy as np
import cv2


def apply_clahe(image: np.ndarray, clip_limit: float = 2.0, tile_grid_size: Tuple[int, int] = (1, 1)) -> np.ndarray:
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab_image)
    l_enhanced = clahe.apply(l)
    enhanced_image = cv2.merge((l_enhanced, a, b))
    enhanced_image = cv2.cvtColor(enhanced_image, cv2.COLOR_LAB2BGR)
    return enhanced_image


def apply_clahe_on_all(image_dir: str, output_dir: str, clip_limit: float = 2.0,
                       tile_grid_size: Tuple[int, int] = (1, 1)) -> None:
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all images in the specified folder (common formats)
    image_paths = glob.glob(os.path.join(image_dir, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png files
    for img_path in image_paths:
        image = cv2.imread(img_path)
        assert image is not None, "Image could not found"
        result = apply_clahe(image, clip_limit, tile_grid_size)

        # Extract filename and define output path
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)

        # Save the mask as a PNG file
        cv2.imwrite(output_path, result)
        print(f"Saved image to {output_path}")
