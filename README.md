# Small library for yolo datasets

## Examples:
### yolo_dataset_redactor.spliterators
VideoSpliterator:
```python
from yolo_dataset_redactor.spliterators import VideoSpliterator

images_path = "./images" # save to this path
period = 10 # every 10 frames saved

video_path = "./videos/some.mp4" # video path

spliterator = VideoSpliterator(images_path, period)

spliterator.split(video_path)
```

VideosSpliterator:
```python
from yolo_dataset_redactor.spliterators import VideosSpliterator

suffixes = ["mp4"] # video suffix for read
images_path = "./images" # save to this path
period = 10 # every 10 frames saved

videos_path = "./videos"

spliterator = VideosSpliterator(suffixes, images_path, period)

spliterator.split(videos_path)
```
### yolo_dataset_redactor
ImagesResizer:
```python
from yolo_dataset_redactor import ImagesResizer

suffixes = ["png"] # video suffix for read
size = (640, 640) # (width, height) to resize

images_path = "./images" # path with images

resizer = ImagesResizer(size, suffixes)

resizer.resize_all_images_in_path(images_path)
```