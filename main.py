import tkinter as tk
from app import VideoDownloaderApp

# 默认参数
DEFAULT_URL = ''
DEFAULT_VIDEO_FORMAT = 'bestvideo'
DEFAULT_AUDIO_FORMAT = 'bestaudio'
DEFAULT_PATH = r'F:\download'


def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root, DEFAULT_URL, DEFAULT_PATH, DEFAULT_VIDEO_FORMAT, DEFAULT_AUDIO_FORMAT)
    root.mainloop()


if __name__ == "__main__":
    main()
