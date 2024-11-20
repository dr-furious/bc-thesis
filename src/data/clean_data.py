import glob
import cv2
import os
import numpy as np


def remove_blackened_images(image_dir: str, threshold: float = 0.05, bin_dir: str = None) -> None:
    if not 0 < threshold < 1:
        raise ValueError(f"Parameter 'threshold' must be from interval (0,1), but is {threshold}.")
    os.makedirs(bin_dir, exist_ok=True)

    # Get all images from a directory
    image_paths = glob.glob(os.path.join(image_dir, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png files
    for image_path in image_paths:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        if np.sum(image == 0)/image.size >= threshold:
            # Remove image with black artifacts
            # os.remove(image_path)
            print(f"Removed {image_path}.")
            if bin_dir is not None:
                bin_path = os.path.join(bin_dir, os.path.basename(image_path))
                cv2.imwrite(bin_path, image)
                print(f"Saved to {bin_path}.")
            return
