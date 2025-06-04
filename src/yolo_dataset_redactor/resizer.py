import os.path
from collections.abc import Sequence

import cv2
import numpy as np

from yolo_dataset_redactor.base import FileFinder


class ImagesResizer:
    def __init__(self, size: Sequence, suffixes: list[str]):
        self.__file_finder = FileFinder(suffixes)
        self.__size = size

    def resize_image(self, image_path: str):
        image = cv2.imdecode(np.fromfile(image_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        image = cv2.resize(image, self.__size)
        goddest, image = cv2.imencode(os.path.splitext(image_path)[1], image)
        if not goddest:
            raise Exception("Could not encode image")
        image.tofile(image_path)

    def resize_all_images_in_path(self, images_path: str):
        files = self.__file_finder.get_all_files_with_true_suffixes(images_path)
        for image_name in files:
            self.resize_image(os.path.join(images_path, image_name))
