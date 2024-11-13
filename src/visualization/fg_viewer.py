import cv2
import numpy as np
import matplotlib.pyplot as plt


def fg_viewer(img_path: str, mask_path: str) -> None:
    # Load the image and mask
    image = cv2.imread(img_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    print(mask)

    # Ensure the mask is binary (0 or 1) if it isn't already
    mask = (mask == 1).astype(np.uint8)  # Converts mask to binary (1 where mask==1, 0 elsewhere)

    # Apply the mask to the image (only keep regions where mask == 1)
    foreground = cv2.bitwise_and(image, image, mask=mask)

    # Display the result
    plt.figure(figsize=(10, 10))
    plt.imshow(cv2.cvtColor(foreground, cv2.COLOR_BGR2RGB))  # Convert BGR to RGB for displaying
    plt.axis('off')
    plt.show()
