import cv2
from numpy import ndarray
from file_classes import FileFinder


class VideoSpliterator:
    def __init__(self, video_path: str, images_path: str, symbol: str, period: int):
        self.video_path = video_path
        self.images_path = images_path
        self.frame: ndarray | None = None
        self.frames: list[ndarray] = []
        self.symbol = symbol
        self.period = period

    def save_frame(self):
        self.frames.append(self.frame)

    def save_all_to_png(self):
        for frame_id in range(len(self.frames)):
            path = f"{self.images_path}/mini_{self.symbol}_{frame_id}.png"
            cv2.imwrite(path, self.frames[frame_id])

    def start_frame_split_loop(self):
        video = cv2.VideoCapture(self.video_path)
        frame_checker = 0
        _, image = video.read()
        while image is not None:
            print(image)
            image = cv2.resize(image, (640, 640))
            self.frame = image
            if frame_checker % self.period == 0:
                self.save_frame()
            frame_checker += 1
            _, image = video.read()


class VideosSpliterator(FileFinder):
    def __init__(self, suffixes: list[str], videos_path: str, images_path: str, period: int):
        super().__init__(suffixes, videos_path)
        self.suffixes = suffixes
        self.videos_path = videos_path
        self.images_path = images_path
        self.period = period

    def split(self):
        for i in range(len(self.all_file_names)):
            name = self.all_file_names[i]
            video_spliter = VideoSpliterator(self.videos_path + name, self.images_path, str(i), self.period)
            video_spliter.start_frame_split_loop()
            video_spliter.save_all_to_png()


def start():
    videos_spliter = VideosSpliterator(["mp4"], "D:/neura_set/videos/", "D:/neura_set/images", 30)
    videos_spliter.find_all_all_file_with_true_suffixes()
    videos_spliter.split()


start()
