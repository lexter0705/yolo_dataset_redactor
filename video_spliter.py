import cv2
from numpy import ndarray
from file_classes import FileFinder


class VideoSpliterator:
    def __init__(self, video_path: str, images_path: str, symbol: str, period: int):
        self.__video_path = video_path
        self.__images_path = images_path
        self.__frames: list[ndarray] = []
        self.__symbol = symbol
        self.__period = period

    def __save_all_to_png(self):
        for frame_id in range(len(self.__frames)):
            path = f"{self.__images_path}/mini_{self.__symbol}_{frame_id}.png"
            cv2.imwrite(path, self.__frames[frame_id])

    def __start_frame_split_loop(self):
        video = cv2.VideoCapture(self.__video_path)
        frame_checker = 0
        _, image = video.read()
        while image is not None:
            _, image = video.read()
            if frame_checker % self.__period == 0:
                self.__frames.append(image)
            frame_checker += 1

    def save_all(self):
        self.__start_frame_split_loop()
        self.__save_all_to_png()


class VideosSpliterator(FileFinder):
    def __init__(self, suffixes: list[str], videos_path: str, images_path: str, period: int):
        super().__init__(suffixes, videos_path)
        self.__suffixes = suffixes
        self.__videos_path = videos_path
        self.__images_path = images_path
        self.__period = period

    def split(self):
        self.find_all_files_with_true_suffixes()
        files = self.get_files_name()
        for i in range(len(files)):
            name = files[i]
            video_spliter = VideoSpliterator(self.__videos_path + name, self.__images_path, str(i), self.__period)
            video_spliter.save_all()
