import cv2
import matplotlib.pyplot as plt
import numpy as np
import os


def image_viewer(path_to_data_image, path_to_label_image, path_to_output_image):
    if not os.path.exists(path_to_data_image):
        print(f"Error: Image file not found at {path_to_data_image}")
        return
    if not os.path.exists(path_to_label_image):
        print(f"Error: Label file not found at {path_to_label_image}")
        return

    # Load the histopathology image and label image
    histopathology_img = cv2.imread(path_to_data_image)
    label_img = cv2.imread(path_to_label_image, cv2.IMREAD_GRAYSCALE)

    # Ensure both images have the same dimensions
    assert histopathology_img.shape[:2] == label_img.shape[:2], "Image and label dimensions do not match."

    # Create a color mask based on different label values
    color_mask = np.zeros_like(histopathology_img)

    # Define colors for each label value
    color_map = {
        1: [0, 255, 255],   # Cyan for label 1
        2: [0, 0, 255],     # Blue for label 2
        3: [128, 0, 128],   # Purple for label 3
        4: [255, 165, 0],   # Orange for label 4
        5: [0, 255, 0],     # Green for label 5
        6: [0, 0, 0],       # Black for label 6
        7: [120, 60, 0],    #
    }

    # Apply the colors to the mask based on the label values
    for label_value, color in color_map.items():
        color_mask[label_img == label_value] = color

    # Overlay the mask on the histopathology image
    overlay_img = cv2.addWeighted(histopathology_img, 0.7, color_mask, 0.3, 0)

    # Create a side-by-side figure
    plt.figure(figsize=(20, 10))

    # Original image
    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(histopathology_img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis('off')

    # Mask image (label image)
    plt.subplot(1, 3, 2)
    plt.imshow(color_mask)
    plt.title("Color Mask")
    plt.axis('off')

    # Overlayed image
    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(overlay_img, cv2.COLOR_BGR2RGB))
    plt.title("Overlay Image")
    plt.axis('off')

    # Show the figure
    plt.tight_layout()
    plt.show()

    # Optionally save the output image
    # cv2.imwrite(path_to_output_image, overlay_img)