import cv2
from collections.abc import Sequence
from file_classes import FileFinder


class ImagesResizer(FileFinder):
    def __init__(self, images_path: str, size: Sequence, suffixes: list[str], save_path: str):
        super().__init__(suffixes, images_path)
        self.__images_path = images_path
        self.__save_path = save_path
        self.__size = size

    def resize_image(self, image_name: str):
        image = cv2.imread(self.__images_path + image_name)
        image = cv2.resize(image, self.__size)
        cv2.imwrite(self.__save_path + image_name, image)

    def resize_all_images_in_path(self):
        self.find_all_files_with_true_suffixes()
        for image_name in self.__all_file_names:
            self.resize_image(image_name)
