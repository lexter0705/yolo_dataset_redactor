from yolo_dataset_redactor.base import FileFinder
from yolo_dataset_redactor.spliterators.base import Spliterator
from yolo_dataset_redactor.spliterators.spliterator import VideoSpliterator

import os

class VideosSpliterator(Spliterator):
    def __init__(self, suffixes: list[str], images_path: str, period: int):
        self.__finder = FileFinder(suffixes)
        self.__video_spliterator = VideoSpliterator(images_path, period)

    def split(self, videos_path: str):
        files = self.__finder.get_all_files_with_true_suffixes(videos_path)
        for f in files:
            self.__video_spliterator.split(os.path.join(videos_path, f))
