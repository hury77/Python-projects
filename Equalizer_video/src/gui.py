import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import threading

class VideoComparerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Comparer")
        self.video_path1 = None
        self.video_path2 = None

        # Create canvas for video 1
        self.canvas1 = tk.Canvas(root, width=400, height=300, bg='black')
        self.canvas1.grid(row=0, column=0, padx=10, pady=10)

        # Create canvas for video 2
        self.canvas2 = tk.Canvas(root, width=400, height=300, bg='black')
        self.canvas2.grid(row=0, column=1, padx=10, pady=10)

        # Create buttons
        self.load_button1 = tk.Button(root, text="Load Video 1", command=self.load_video1)
        self.load_button1.grid(row=1, column=0, pady=10)

        self.load_button2 = tk.Button(root, text="Load Video 2", command=self.load_video2)
        self.load_button2.grid(row=1, column=1, pady=10)

        self.play_button = tk.Button(root, text="Play", command=self.play_videos)
        self.play_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_videos)
        self.pause_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_videos)
        self.stop_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.cap1 = None
        self.cap2 = None
        self.playing = False

    def load_video1(self):
        self.video_path1 = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mov *.mxf")])
        print(f"Loaded video 1: {self.video_path1}")

    def load_video2(self):
        self.video_path2 = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.mov *.mxf")])
        print(f"Loaded video 2: {self.video_path2}")

    def play_videos(self):
        if self.video_path1 and self.video_path2:
            self.cap1 = cv2.VideoCapture(self.video_path1)
            self.cap2 = cv2.VideoCapture(self.video_path2)
            self.playing = True
            threading.Thread(target=self.update_frames).start()

    def update_frames(self):
        while self.playing:
            ret1, frame1 = self.cap1.read()
            ret2, frame2 = self.cap2.read()

            if not ret1 or frame1 is None:
                print("Video 1 ended or frame is empty")
                break

            if not ret2 or frame2 is None:
                print("Video 2 ended or frame is empty")
                break

            # Convert frames to RGB
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

            # Convert frames to ImageTk format
            img1 = ImageTk.PhotoImage(Image.fromarray(frame1))
            img2 = ImageTk.PhotoImage(Image.fromarray(frame2))

            # Update canvases
            self.canvas1.create_image(0, 0, anchor=tk.NW, image=img1)
            self.canvas2.create_image(0, 0, anchor=tk.NW, image=img2)

            self.root.update()

        self.cap1.release()
        self.cap2.release()

    def pause_videos(self):
        self.playing = False

    def stop_videos(self):
        self.playing = False
        if self.cap1:
            self.cap1.release()
        if self.cap2:
            self.cap2.release()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoComparerGUI(root)
    root.mainloop()