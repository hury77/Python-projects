import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image, ImageTk
import cv2
import threading
import os
import queue

class VideoComparerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Comparer")
        self.video_path1 = None
        self.video_path2 = None

        # Configure grid for responsiveness
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=3)
        self.root.rowconfigure(1, weight=0)

        # Canvas size
        self.canvas_size = (800, 450)

        # Create canvas for video 1
        self.canvas1 = tk.Canvas(root, bg='black', width=self.canvas_size[0], height=self.canvas_size[1])
        self.canvas1.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # Create canvas for video 2
        self.canvas2 = tk.Canvas(root, bg='black', width=self.canvas_size[0], height=self.canvas_size[1])
        self.canvas2.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Create progress bar
        self.progress = ttk.Scale(root, from_=0, to=100, orient="horizontal", command=self.seek_video)
        self.progress.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=5)

        # Load control button icons
        ICON_PATH = os.path.join(os.path.dirname(__file__), "icons")
        self.play_icon = self.resize_icon(os.path.join(ICON_PATH, "play.png"), (32, 32))
        self.pause_icon = self.resize_icon(os.path.join(ICON_PATH, "pause.png"), (32, 32))
        self.stop_icon = self.resize_icon(os.path.join(ICON_PATH, "stop.png"), (32, 32))
        self.open_icon = self.resize_icon(os.path.join(ICON_PATH, "open.png"), (32, 32))

        # Create buttons in a horizontal frame
        self.controls_frame = tk.Frame(root)
        self.controls_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

        self.load_button1 = tk.Button(self.controls_frame, image=self.open_icon, command=self.load_video1)
        self.load_button1.grid(row=0, column=0, padx=5)

        self.load_button2 = tk.Button(self.controls_frame, image=self.open_icon, command=self.load_video2)
        self.load_button2.grid(row=0, column=1, padx=5)

        self.play_button = tk.Button(self.controls_frame, image=self.play_icon, command=self.play_videos)
        self.play_button.grid(row=0, column=2, padx=5)

        self.pause_button = tk.Button(self.controls_frame, image=self.pause_icon, command=self.pause_videos)
        self.pause_button.grid(row=0, column=3, padx=5)

        self.stop_button = tk.Button(self.controls_frame, image=self.stop_icon, command=self.stop_videos)
        self.stop_button.grid(row=0, column=4, padx=5)

        # Video capture objects and flags
        self.cap1 = None
        self.cap2 = None
        self.playing = False

        # Queue for thread-safe communication
        self.frame_queue1 = queue.Queue()
        self.frame_queue2 = queue.Queue()

    def resize_icon(self, filepath, size):
        """Resize an icon to the specified size using PIL."""
        img = Image.open(filepath)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)

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

            # Start threads for reading frames
            threading.Thread(target=self.read_frames, args=(self.cap1, self.frame_queue1)).start()
            threading.Thread(target=self.read_frames, args=(self.cap2, self.frame_queue2)).start()

            # Start updating frames in the GUI
            self.update_frames()

    def read_frames(self, cap, frame_queue):
        """Read frames from a video capture object and put them into a queue."""
        while self.playing:
            ret, frame = cap.read()
            if not ret:
                break
            frame_queue.put(frame)
        cap.release()

    def update_frames(self):
        """Update frames on the canvas."""
        if not self.playing:
            return

        try:
            if not self.frame_queue1.empty() and not self.frame_queue2.empty():
                frame1 = self.frame_queue1.get()
                frame2 = self.frame_queue2.get()

                # Resize frames to fit canvas
                frame1 = cv2.resize(frame1, self.canvas_size)
                frame2 = cv2.resize(frame2, self.canvas_size)

                # Convert frames to RGB
                frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
                frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

                # Convert frames to ImageTk format
                img1 = ImageTk.PhotoImage(Image.fromarray(frame1))
                img2 = ImageTk.PhotoImage(Image.fromarray(frame2))

                # Update canvases
                self.canvas1.create_image(0, 0, anchor=tk.NW, image=img1)
                self.canvas2.create_image(0, 0, anchor=tk.NW, image=img2)

                # Keep reference to prevent garbage collection
                self.canvas1.image = img1
                self.canvas2.image = img2
        except Exception as e:
            print(f"Error updating frames: {e}")

        # Schedule next frame update
        self.root.after(10, self.update_frames)

    def pause_videos(self):
        self.playing = False

    def stop_videos(self):
        self.playing = False
        if self.cap1:
            self.cap1.release()
        if self.cap2:
            self.cap2.release()

    def seek_video(self, value):
        if self.cap1 and self.cap2:
            # Implement seeking logic here
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoComparerGUI(root)
    root.mainloop()