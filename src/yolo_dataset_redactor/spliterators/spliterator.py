import os

import cv2

from yolo_dataset_redactor.spliterators.base import Spliterator


class VideoSpliterator(Spliterator):
    def __init__(self,
                 images_path: str,
                 period: int = 10):
        self.__images_path = images_path
        self.__period = period

    def split(self, video_path: str):
        video = cv2.VideoCapture(video_path)
        video_name = os.path.basename(video_path)
        frame_checker = 0
        _, image = video.read()
        while image is not None:
            _, image = video.read()
            if frame_checker % self.__period == 0:
                path = f"{self.__images_path}/{video_name}_{frame_checker}.png"
                goddest, image = cv2.imencode(os.path.splitext(path)[1], image)
                if not goddest:
                    raise Exception("Could not encode image")
                image.tofile(path)
            frame_checker += 1
