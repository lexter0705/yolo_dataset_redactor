import cv2
from collections.abc import Sequence
from file_classes import FileFinder


class ImagesResizer(FileFinder):
    def __init__(self, images_path: str, size: Sequence, suffixes: list[str], save_path: str):
        super().__init__(suffixes, images_path)
        self.images_path = images_path
        self.save_path = save_path
        self.size = size

    def resize_image(self, image_name: str):
        image = cv2.imread(self.images_path + image_name)
        image = cv2.resize(image, self.size)
        cv2.imwrite(self.save_path + image_name, image)

    def resize_all_images_in_path(self):
        self.find_all_all_file_with_true_suffixes()
        for image_name in self.all_file_names:
            self.resize_image(image_name)
