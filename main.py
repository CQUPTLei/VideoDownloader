# -*- coding = utf-8 -*-
# @TIME : 2024/07/08 18:30
# @Author : Grace
# @File : main.py
# @Software : PyCharm
# Overview：Video download app with yt_dlp.

import tkinter as tk
# fixed window size
from app import VideoDownloaderApp
# Flexible window size
# from app_flexible_window import VideoDownloaderApp

DEFAULT_URL = ''
# Default video format code
DEFAULT_VIDEO_FORMAT = 'bestvideo'
# Default audio format code
DEFAULT_AUDIO_FORMAT = 'bestaudio'
# Default video save path
DEFAULT_PATH = r'F:\download'


def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root, DEFAULT_URL, DEFAULT_PATH, DEFAULT_VIDEO_FORMAT, DEFAULT_AUDIO_FORMAT)
    root.mainloop()


if __name__ == "__main__":
    main()
