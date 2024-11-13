import os
import glob
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from typing import Tuple


def use_grabcut(image: np.ndarray, iterations_count: int, corner_size=1) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    fg_model: np.ndarray = np.zeros((1, 65), np.float64)
    bg_model: np.ndarray = np.zeros((1, 65), np.float64)

    # Initialize the mask with probable foreground everywhere
    mask: np.ndarray = np.ones(image.shape[:2], np.uint8) * cv.GC_PR_FGD

    # Set corners as definite background
    h, w = mask.shape
    mask[:corner_size, :corner_size] = cv.GC_BGD  # Top-left corner
    mask[:corner_size, w - corner_size:] = cv.GC_BGD  # Top-right corner
    mask[h - corner_size:, :corner_size] = cv.GC_BGD  # Bottom-left corner
    mask[h - corner_size:, w - corner_size:] = cv.GC_BGD  # Bottom-right corner

    mask, bg_model, fg_model = cv.grabCut(image, mask, None, bg_model, fg_model, iterations_count,
                                          cv.GC_INIT_WITH_MASK)
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = image * mask[:, :, np.newaxis]
    plt.imshow(img), plt.colorbar(), plt.show()

    return mask, bg_model, fg_model


def use_grabcut_on_all(image_folder: str, output_dir: str, iterations_count: int = 5) -> None:
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all images in the specified folder (common formats)
    image_paths = glob.glob(os.path.join(image_folder, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png files
    counter = 10
    for img_path in image_paths:
        image = cv.imread(img_path)
        assert image is not None, "Image could not found"
        mask, bg_model, fg_model = use_grabcut(image, iterations_count)

        # Extract filename and define output path
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)
        counter-=1
        if counter == 0:
            return
        # Save the mask as a PNG file
        cv.imwrite(output_path, mask)
        print(f"Saved mask to {output_path}")
