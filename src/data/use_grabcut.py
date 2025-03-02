import os
import glob
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
from typing import Tuple


def use_grabcut(image: np.ndarray, iterations_count: int, brightest_pixels_bg: int) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    fg_model: np.ndarray = np.zeros((1, 65), np.float64)
    bg_model: np.ndarray = np.zeros((1, 65), np.float64)

    mask = create_mask(image, brightest_pixels_bg)

    mask, bg_model, fg_model = cv.grabCut(image, mask, None, bg_model, fg_model, iterations_count,
                                          cv.GC_INIT_WITH_MASK)

    # Visualize
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img = image * mask[:, :, np.newaxis]
    # plt.imshow(img), plt.colorbar(), plt.show()

    return mask, bg_model, fg_model


def use_grabcut_on_all(image_folder: str, output_dir: str, brightest_pixels_bg: int, iterations_count: int = 5) -> None:
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Find all images in the specified folder (common formats)
    image_paths = glob.glob(os.path.join(image_folder, '*.[jp][pn]g'))  # Matches .jpg, .jpeg, .png files
    counter = 100
    for img_path in image_paths:
        image = cv.imread(img_path)
        assert image is not None, "Image could not found"
        mask, bg_model, fg_model = use_grabcut(image, iterations_count, brightest_pixels_bg)

        # Extract filename and define output path
        filename = os.path.basename(img_path)
        output_path = os.path.join(output_dir, filename)
        counter-=1
        if counter == 0:
            #return
            pass
        # Save the mask as a PNG file
        cv.imwrite(output_path, mask)
        print(f"Saved mask to {output_path}")


def create_mask(image: np.ndarray, num_brightest: int = 20) -> np.ndarray:
    # Ensure the image is in color
    assert len(image.shape) == 3 and image.shape[2] == 3, "Image must be a color image (3 channels)."

    # Convert the image to grayscale for brightness computation
    grayscale_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Initialize the mask with probable foreground everywhere
    mask = np.ones(grayscale_image.shape, np.uint8) * cv.GC_PR_FGD  # Default to probable foreground

    # Flatten the grayscale image to find the brightest pixel values
    flat_indices = np.argsort(grayscale_image.ravel())[::-1]  # Indices sorted in descending order
    brightest_indices = flat_indices[:num_brightest]  # Take the top `num_brightest`

    # Convert flat indices to 2D coordinates
    brightest_coords = np.unravel_index(brightest_indices, grayscale_image.shape)

    # Update the mask for the brightest pixels
    rows, cols = brightest_coords  # Extract row and column indices
    mask[rows, cols] = cv.GC_BGD  # Mark these pixels as definite foreground

    return mask
