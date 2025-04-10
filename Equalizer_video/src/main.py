import tkinter as tk
from gui import VideoComparerGUI

def main():
    root = tk.Tk()
    app = VideoComparerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()