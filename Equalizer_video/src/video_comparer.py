import cv2
import time

class VideoComparer:
    def __init__(self, video_path1, video_path2):
        self.video_path1 = video_path1
        self.video_path2 = video_path2
        self.cap1 = cv2.VideoCapture(video_path1)
        self.cap2 = cv2.VideoCapture(video_path2)

        # Ustawienia synchronizacji FPS
        # ...

    def play(self):
        self.playing = True
        while self.playing:
            # Pobieranie i wyświetlanie klatek
            # ...

if __name__ == "__main__":
    comparer = VideoComparer("video1.mp4", "video2.mp4")
    comparer.play()