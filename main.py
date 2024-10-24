from src.features.crop_rois import image_rois_from_coco_json


def main():
    image_name = "TCGA-A2-A0CM-01Z-00-DX1.AC4901DE-4B6D-4185-BB9F-156033839828_[9283, 28428, 11819, 30374].png"
    image_name_1 = "100B_[10779, 11621, 12102, 12874].png"
    image_path_bcss = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-bcss/images/" + image_name
    label_path_bcss = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-bcss/masks/" + image_name

    image_path_cells = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-cells/images/" + image_name_1
    label_path_cells = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-cells/masks/" + image_name_1

    # image_viewer(image_path_cells, label_path_cells, None)
    # image_viewer(image_path_bcss, label_path_bcss, None)

    path_to_coco_json = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-cells/tiger-coco.json"
    path_to_images = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-cells/"
    output_dir = "data/processed/cropped_cell_rois/"
    image_rois_from_coco_json(json_path=path_to_coco_json, image_dir=path_to_images, output_dir=output_dir)


if __name__ == '__main__':
    main()
