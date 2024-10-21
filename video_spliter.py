import cv2
from numpy import ndarray
from file_classes import FileFinder


class VideoSpliterator:
    def __init__(self, video_path: str, images_path: str, symbol: str, period: int):
        self.__video_path = video_path
        self.__images_path = images_path
        self.__frame: ndarray | None = None
        self.__frames: list[ndarray] = []
        self.__symbol = symbol
        self.__period = period

    def save_frame(self):
        self.__frames.append(self.__frame)

    def save_all_to_png(self):
        for frame_id in range(len(self.__frames)):
            path = f"{self.__images_path}/mini_{self.__symbol}_{frame_id}.png"
            cv2.imwrite(path, self.__frames[frame_id])

    def start_frame_split_loop(self):
        video = cv2.VideoCapture(self.__video_path)
        frame_checker = 0
        _, image = video.read()
        while image is not None:
            print(image)
            image = cv2.resize(image, (640, 640))
            self.__frame = image
            if frame_checker % self.__period == 0:
                self.save_frame()
            frame_checker += 1
            _, image = video.read()


class VideosSpliterator(FileFinder):
    def __init__(self, suffixes: list[str], videos_path: str, images_path: str, period: int):
        super().__init__(suffixes, videos_path)
        self.__suffixes = suffixes
        self.__videos_path = videos_path
        self.__images_path = images_path
        self.__period = period

    def split(self):
        for i in range(len(self.__all_file_names)):
            name = self.__all_file_names[i]
            video_spliter = VideoSpliterator(self.__videos_path + name, self.__images_path, str(i), self.__period)
            video_spliter.start_frame_split_loop()
            video_spliter.save_all_to_png()
