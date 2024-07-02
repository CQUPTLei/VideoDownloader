import tkinter as tk
from tkinter import filedialog
import subprocess
import threading
import yt_dlp
from logger import MyLogger


# 创建主窗口0
class VideoDownloaderApp:
    def __init__(self, root, url, path, vformat, aformat):
        self.log = None
        self.root = root
        self.root.title('视频下载程序')
        self.window_set(root, 900, 500)
        # 初始化参数
        self.url = tk.StringVar(value=url)
        self.path = tk.StringVar(value=path)
        self.video_format = tk.StringVar(value=vformat)
        self.audio_format = tk.StringVar(value=aformat)
        # 用户界面元素
        self.create_ui()

    # 设置窗口大小，位置
    @staticmethod
    def window_set(root, width, height):
        screenwidth = root.winfo_screenwidth()  # 获取显示器尺寸
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 5)
        root.geometry(size)
        root.update()

    def create_ui(self):
        # 输入视频URL
        url_label = tk.Label(self.root, text='输入视频URL', font=("Roboto", 12))
        url_label.place(x=10, y=10)

        url_entry = tk.Entry(self.root, textvariable=self.url, bg='#FAFAD2')
        url_entry.place(x=110, y=5, width=600, height=40)

        url_button = tk.Button(self.root, text='确定', bg='#FFE4C4', command=self.url_input)
        url_button.place(x=710, y=5, width=90, height=40)

        # 获取视频信息按钮
        info_button = tk.Button(self.root, text='获取视频信息', bg='#FFD39B', command=self.print_info)
        info_button.place(x=800, y=5, width=90, height=40)

        # 选择保存路径
        path_label = tk.Label(self.root, text='视频保存路径', font=("Roboto", 12))
        path_label.place(x=10, y=60)

        path_entry = tk.Entry(self.root, textvariable=self.path, bg='#00CD66', font=('FangSong', 10), state='readonly')
        path_entry.place(x=110, y=55, width=600, height=40)

        path_button = tk.Button(self.root, text='选择路径', bg='#C1CDC1', command=self.select_path)
        path_button.place(x=710, y=55, width=180, height=40)

        # 自定义选择音视频质量
        format_label = tk.Label(self.root, text='自定义格式', font=("Roboto", 12))
        format_label.place(x=10, y=110)

        video_label = tk.Label(self.root, text='视频', bg='#EEAD0E', font=("Roboto", 12))
        video_label.place(x=110, y=110, width=50, height=40)

        video_entry = tk.Entry(self.root, textvariable=self.video_format, bg='#E6E6FA')
        video_entry.place(x=160, y=110, width=250, height=40)

        audio_label = tk.Label(self.root, text='音频', bg='#9932CC', font=("Roboto", 12))
        audio_label.place(x=410, y=110, width=50, height=40)

        audio_entry = tk.Entry(self.root, textvariable=self.audio_format, bg='#E6E6FA')
        audio_entry.place(x=460, y=110, width=250, height=40)

        format_button = tk.Button(self.root, text='确定', bg='#EEB4B4', command=self.select_format)
        format_button.place(x=710, y=110, width=90, height=40)

        dl_button = tk.Button(self.root, text='开始下载', bg='#00FF00', font=('楷体', 14),
                              command=self.start_download)
        dl_button.place(x=800, y=110, width=90, height=40)

        dl_txt = tk.Label(self.root,
                          text='输入URL后必须点击确定，可以不指定音视频质量(获取视频信息后的ID)，默认下载最高质量音视频，由ffmpeg自动合并',
                          font=('FangSong', 12), bg='#FFFFF0')
        dl_txt.place(x=10, y=155, width=880, height=40)

        # 日志输出框
        self.log = tk.Text(self.root, bg='black', fg='#00CD00', wrap='word')
        self.log.place(x=10, y=200, width=880, height=290)
        self.log.insert(tk.END,
                        '     -----------------------------------------Hello，welcome to video downloader'
                        '-----------------------------------------\n')

    # 视频地址输入
    def url_input(self):
        self.url.set(self.url.get().replace('&', '"&"'))  # URL中&不可用于shell

    # 选择视频保存路径
    def select_path(self):
        path = filedialog.askdirectory(title='请选择一个目录')
        if path:
            self.path.set(path)

    # 打印选择的视频格式（品质）
    def select_format(self):
        video_format = self.video_format.get()
        audio_format = self.audio_format.get()
        quality = video_format if not audio_format else audio_format if not video_format else video_format + '+' + audio_format
        # 日志中显示所选格式
        self.log.insert(tk.END, f'已选择音视频格式：{quality}\n')

    def print_info(self):
        thread = threading.Thread(target=self.get_info)
        thread.start()

    def get_info(self):
        info_win = tk.Toplevel(self.root)
        info_win.geometry('1000x600')
        info_win.config(background='#CCCCFF')
        info_win.title('该视频的详细信息')
        info_txt = tk.Text(info_win, bg='#CCCCFF', fg='#000000', font=("Roboto", 12), wrap='word')
        info_txt.place(relx=0, y=0, relheight=1, relwidth=1)
        info_txt.insert(tk.END, '正在获取该视频的格式信息...')
        venv_path = r'D:\anaconda\envs\pylearn\pythonw.exe'
        cmd = [venv_path, '-m', 'yt_dlp', '-F', self.url.get()]
        return_code = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
        # return_code = subprocess.run(['yt-dlp', '-F', self.url.get()], stdout=subprocess.PIPE)
        res = return_code.stdout
        info_txt.insert(tk.END, res)

    def start_download(self):
        self.log.insert(tk.END, '开始下载...\n')
        thread = threading.Thread(target=self.download_thread)
        thread.start()

    def download_thread(self):
        try:
            video = self.video_format.get()
            audio = self.audio_format.get()
            # 检查是否有输入，如果有输入则添加到列表中
            Q = audio if not video else video if not audio else video + '+' + audio
            # Q = (self.video_format.get(), '+', self.audio_format.get())
            Q = "".join(Q)

            download_opts = {
                'proxy': '127.0.0.1:8889',
                'format': Q,
                'paths': {'home': self.path.get()},
                'extractor_retries': 10,
                'no_warnings': True,
                'ignoreerrors': 'only_download',
                'wait_for_video': (20, 30),
                'retries': 15,
                'fragment_retries': 10,
                'file_access_retries': 10,
                'continuedl': True,
                'continue': True,
                'noprogress': False,
                'consoletitle': False,
                'logger': MyLogger(self.log),
            }

            with yt_dlp.YoutubeDL(download_opts) as ydl:
                ydl.download([self.url.get()])

            self.log.insert(tk.END, '下载完成。\n')
        except Exception as e:
            self.log.insert(tk.END, f'下载出现错误：{str(e)}\n')
