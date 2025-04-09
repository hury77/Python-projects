import cv2
import time

class VideoComparer:
    def __init__(self, video_path1, video_path2):
        self.video_path1 = video_path1
        self.video_path2 = video_path2
        self.cap1 = cv2.VideoCapture(video_path1)
        self.cap2 = cv2.VideoCapture(video_path2)

        # Force FFmpeg to use a single thread
        self.cap1.set(cv2.CAP_PROP_THREAD_COUNT, 1)
        self.cap2.set(cv2.CAP_PROP_THREAD_COUNT, 1)

        self.playing = False

        # Get FPS for both videos
        self.fps1 = self.cap1.get(cv2.CAP_PROP_FPS) or 30  # Default to 30 if FPS is not available
        self.fps2 = self.cap2.get(cv2.CAP_PROP_FPS) or 30  # Default to 30 if FPS is not available

    def play(self):
        self.playing = True
        while self.playing:
            start_time = time.time()

            # Read frames from both videos
            ret1, frame1 = self.cap1.read()
            ret2, frame2 = self.cap2.read()

            # If either video is finished, stop playback
            if not ret1 or not ret2:
                print("One of the videos has finished playing.")
                break

            # Display both frames
            cv2.imshow('Video 1', frame1)
            cv2.imshow('Video 2', frame2)

            # Calculate delay to synchronize FPS
            elapsed_time = time.time() - start_time
            delay1 = max(1, int((1 / self.fps1 - elapsed_time) * 1000))
            delay2 = max(1, int((1 / self.fps2 - elapsed_time) * 1000))
            cv2.waitKey(min(delay1, delay2))

        self.cap1.release()
        self.cap2.release()
        cv2.destroyAllWindows()

    def pause(self):
        self.playing = False

    def stop(self):
        self.playing = False
        self.cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
        cv2.destroyAllWindows()