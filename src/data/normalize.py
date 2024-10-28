from ..utils.load_json import load_json
import cv2
import os
import torch
from torchvision import transforms
import torchstain


def normalize(json_path: str, img_dir: str, output_img_dir: str, target_img_id: int = 1) -> None:
    data = load_json(json_path)

    T = transforms.Compose([
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x * 255)
    ])

    # Loading the target img
    target_img = cv2.imread(os.path.join(img_dir, data['images']['id' == target_img_id]['file_name']))
    target_img = cv2.cvtColor(target_img, cv2.COLOR_BGR2RGB)

    # Preparing normalizer
    normalizer = torchstain.normalizers.MacenkoNormalizer(backend='torch')
    normalizer.fit(T(target_img))

    for img_info in data['images']:
        img_file = img_info['file_name']
        img_path = os.path.join(img_dir, img_file)
        output_path = os.path.join(output_img_dir, img_file)

        # Create directories if they do not exist
        os.makedirs(output_img_dir, exist_ok=True)

        # Load the img to normalize
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = T(img)

        # Apply normalization
        norm_img_tensor, H, E = normalizer.normalize(I=img, stains=True)
        norm_img = norm_img_tensor.cpu().numpy()

        # Save normalized image
        cv2.imwrite(output_path, norm_img)

        print(output_path)



