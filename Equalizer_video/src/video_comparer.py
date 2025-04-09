import cv2

class VideoComparer:
    def __init__(self, video_path1, video_path2):
        self.video_path1 = video_path1
        self.video_path2 = video_path2
        self.cap1 = cv2.VideoCapture(video_path1)
        self.cap2 = cv2.VideoCapture(video_path2)
        self.playing = False

    def play(self):
        self.playing = True
        while self.playing:
            ret1, frame1 = self.cap1.read()
            ret2, frame2 = self.cap2.read()

            # Check if frames are read correctly
            if not ret1 or frame1 is None:
                print(f"Error reading video 1: {self.video_path1}")
                break
            
            if not ret2 or frame2 is None:
                print(f"Error reading video 2: {self.video_path2}")
                break

            # Log frame dimensions for debugging
            print(f"Frame 1 shape: {frame1.shape if frame1 is not None else 'None'}")
            print(f"Frame 2 shape: {frame2.shape if frame2 is not None else 'None'}")

            try:
                cv2.imshow('Video 1', frame1)
                cv2.imshow('Video 2', frame2)
            except cv2.error as e:
                print(f"Error displaying frames: {e}")
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

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