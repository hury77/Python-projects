from gui import VideoComparerGUI
import tkinter as tk

def main():
    root = tk.Tk()
    app = VideoComparerGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()