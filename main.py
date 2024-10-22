from image_viewer import image_viewer


def main():
    image_name = "TCGA-A2-A0CM-01Z-00-DX1.AC4901DE-4B6D-4185-BB9F-156033839828_[9283, 28428, 11819, 30374].png"
    image_name_1 = "100B_[10779, 11621, 12102, 12874].png"
    image_path_bcss = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-bcss/images/" + image_name
    label_path_bcss = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-bcss/masks/" + image_name

    image_path_cells = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-cells/images/" + image_name_1
    label_path_cells = "./../tiger-datasets/wsirois/roi-level-annotations/tissue-cells/masks/" + image_name_1

    # image_viewer(image_path_cells, label_path_cells, None)
    image_viewer(image_path_bcss, label_path_bcss, None)


if __name__ == '__main__':
    main()
