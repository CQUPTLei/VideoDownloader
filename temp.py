import subprocess
from tkinter import filedialog
import yt_dlp


# 打包命令示例，安装pyinstaller，路径自己更改
# pyinstaller -F --paths=C:\Users\14134\.conda\envs\ytdlp\Lib\site-packages --python=C:\Users\14134\.conda\envs\ytdlp\pythonw.exe  --noconsole  --icon=1.ico --name=Downloader DLP_GUI_Perfect.py


# 默认参数
DEFAULT_URL = ''
DEFAULT_VIDEO_FORMAT = 'bestvideo'
DEFAULT_AUDIO_FORMAT = 'bestaudio'
DEFAULT_PATH = r'F:\download'


def main():
    root = tk.Tk()
    app = VideoDownloaderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
