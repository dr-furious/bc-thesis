from ..utils.load_json import load_json
import os
from torchvision import transforms
import torchstain
import cv2


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
    normalizer = torchstain.normalizers.MultiMacenkoNormalizer('avg-post')
    normalizer.fit(T(target_img))

    h_dir = os.path.join(output_img_dir, "hematoxylin")
    e_dir = os.path.join(output_img_dir, "eosin")

    for img_info in data['images']:
        img_file = img_info['file_name']
        img_path = os.path.join(img_dir, img_file)
        output_path = os.path.join(output_img_dir, img_file)
        output_path_h = os.path.join(h_dir, img_file)
        output_path_e = os.path.join(e_dir, img_file)

        # Create directories if they do not exist
        os.makedirs(output_img_dir, exist_ok=True)
        os.makedirs(h_dir, exist_ok=True)
        os.makedirs(e_dir, exist_ok=True)

        # Load the img to normalize
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = T(img)

        # Apply normalization
        norm_img_tensor, hematoxylin, eosin = normalizer.normalize(I=img, stains=True)
        norm_img = norm_img_tensor.cpu().numpy()
        hematoxylin_img = hematoxylin.cpu().numpy()
        eosin_img = eosin.cpu().numpy()

        # Save normalized image
        cv2.imwrite(output_path, norm_img)
        cv2.imwrite(output_path_h, hematoxylin_img)
        cv2.imwrite(output_path_e, eosin_img)

        print(output_path)
        print(output_path_h)
        print(output_path_e)




