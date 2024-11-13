from src.data.crop_rois import image_rois_from_coco_json
from src.visualization.image_viewer import image_viewer
from src.data.normalize import normalize
from src.data.use_grabcut import use_grabcut_on_all
from src.visualization.fg_viewer import fg_viewer


def main():
    image_name = "TCGA-A1-A0SK-01Z-00-DX1.A44D70FA-4D96-43F4-9DD7-A61535786297_[22877, 12530, 24892, 13993].png"
    image_path_bcss = f"./data/raw/tiger-datasets/wsirois/roi-level-annotations/tissue-bcss/images/{image_name}"
    label_path_bcss = f"./data/raw/tiger-datasets/wsirois/roi-level-annotations/tissue-bcss/masks/{image_name}"

    # image_viewer(image_path_bcss, label_path_bcss, None)

    path_to_coco_json = "./data/raw/tiger-datasets/wsirois/roi-level-annotations/tissue-cells/tiger-coco.json"
    path_to_images = "./data/raw/tiger-datasets/wsirois/roi-level-annotations/tissue-cells/"

    # Normalize H&C images using Macenko normalization
    # normalize(json_path=path_to_coco_json, img_dir=path_to_images, output_img_dir="data/processed/normalized_images/")

    path_to_images_cut = "./data/processed/normalized_images"

    output_img_cropped_dir = "data/processed/cropped_cell_rois"
    output_img_grabcut_masks_dir = "data/processed/grab_cut_masks"

    # Crop ROIS from image using COCO JSON annotations
    # image_rois_from_coco_json(json_path=path_to_coco_json,
    #                          image_dir=path_to_images_cut,
    #                          output_dir=output_img_cropped_dir, limit=5000)

    # Call GrabCut algorithm
    use_grabcut_on_all(image_folder=output_img_cropped_dir, output_dir=output_img_grabcut_masks_dir, iterations_count=20)

    # Visualize grabCut results
    # fg_viewer(f"{output_img_cropped_dir}/100B_[21444, 12438, 22739, 13618]_-_183_1051_18_18.png",
    #          f"{output_img_grabcut_masks_dir}/100B_[21444, 12438, 22739, 13618]_-_183_1051_18_18.png")




if __name__ == '__main__':
    main()
