# -*- coding = utf-8 -*-
# @TIME : 2024/07/08 18:30
# @Author : Grace
# @File : app.py
# @Software : PyCharm
# Overview： The main implementation part of the program(flexible windows size).

import threading
import yt_dlp
from tkinter import filedialog
from logger import *
from get_video_info import get_video_formats


class VideoDownloaderApp:
    """A class of Video Downloader Application."""
    def __init__(self, root, url, path, vformat, aformat):
        """
        :param root: tkinter.TK(), the root window of the Tkinter application.
        :param url: str, the URL of the video to be downloaded.
        :param path: str, the path where the video will be saved.
        :param vformat: str,the format of the video (get from video information page, default: 'bestvideo').
        :param aformat: str, the format of the audio (get from video information page, default: 'bestaudio').
        """
        self.log = None
        self.root = root
        self.root.title('VideoDownloader')
        self.window_set(900, 500)
        # 初始化下载参数
        self.url = tk.StringVar(value=url)
        self.path = tk.StringVar(value=path)
        self.video_format = tk.StringVar(value=vformat)
        self.audio_format = tk.StringVar(value=aformat)
        # 用户界面
        self.create_ui()

    def window_set(self, width, height):
        """
        Set size and default location of the window.
        :param width: width of the window.
        :param height: height of the window.
        """
        screenwidth = self.root.winfo_screenwidth()  # 获取显示器分辨率
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 4)
        # Set geometry to NEWGEOMETRY of the form = widthxheight+x+y.
        self.root.geometry(size)
        self.root.update()

    def create_ui(self):
        """Main page of the App(flexible window size)."""
        # 输入视频URL
        url_label = tk.Label(self.root, text='Video URL', font=("Roboto", 12))
        url_label.grid(row=0, column=0, padx=0, pady=10, sticky="nsew")

        url_entry = tk.Entry(self.root, textvariable=self.url, bg='#FAFAD2')
        url_entry.grid(row=0, column=1, padx=0, pady=10, sticky="nsew", columnspan=4)

        url_button = tk.Button(self.root, text='Confirm', bg='#FFE4C4', command=self.url_input)
        url_button.grid(row=0, column=5, padx=0, pady=10, sticky="nsew")

        info_button = tk.Button(self.root, text='Get video info', bg='#FFD39B', command=self.print_info)
        info_button.grid(row=0, column=6, padx=10, pady=10, sticky="nsew")

        # 选择保存路径部分
        path_label = tk.Label(self.root, text='Saved path', font=("Roboto", 12))
        path_label.grid(row=1, column=0, padx=0, pady=0, sticky="nsew")

        path_entry = tk.Entry(self.root, textvariable=self.path, bg='#00CD66', font=('FangSong', 10), state='readonly')
        path_entry.grid(row=1, column=1, padx=0, pady=0, sticky="nsew", columnspan=4)

        path_button = tk.Button(self.root, text='Select the path to save the video', bg='#C1CDC1',
                                command=self.select_path)
        path_button.grid(row=1, column=5, padx=10, pady=0, sticky="nsew", columnspan=2)

        # 自定义选择音视频质量部分
        format_label = tk.Label(self.root, text='Custom Format', font=("Roboto", 12))
        format_label.grid(row=2, column=0, padx=0, pady=10, sticky="nsew")

        video_label = tk.Label(self.root, text='Video', bg='#EEAD0E', font=("Roboto", 12))
        video_label.grid(row=2, column=1, padx=0, pady=10, sticky="nsew")

        video_entry = tk.Entry(self.root, textvariable=self.video_format, bg='#E6E6FA')
        video_entry.grid(row=2, column=2, padx=0, pady=10, sticky="nsew")

        audio_label = tk.Label(self.root, text='Audio', bg='#9932CC', font=("Roboto", 12))
        audio_label.grid(row=2, column=3, padx=0, pady=10, sticky="nsew")

        audio_entry = tk.Entry(self.root, textvariable=self.audio_format, bg='#E6E6FA')
        audio_entry.grid(row=2, column=4, padx=0, pady=10, sticky="nsew")

        format_button = tk.Button(self.root, text='Confirm', bg='#EEB4B4', command=self.select_format)
        format_button.grid(row=2, column=5, padx=0, pady=10, sticky="nsew")

        dl_button = tk.Button(self.root, text='Start  download', bg='#008B00', font=('Impact', 13),
                              command=self.start_download)
        dl_button.grid(row=2, column=6, padx=10, pady=10, sticky="nsew")

        dl_txt = tk.Label(self.root,
                          text='Enter the URL and click OK. The highest quality audio and video will be downloaded and merged by ffmpeg by default.',
                          font=('FangSong', 8), bg='#FFFFF0')
        dl_txt.grid(row=3, column=0, padx=10, pady=0, sticky="ew", columnspan=7)

        # 日志输出框
        self.log = tk.Text(self.root, bg='black', fg='#00CD00', wrap='word')
        self.log.grid(row=4, column=0, columnspan=7, padx=10, pady=5, sticky="nsew")
        self.log.insert(tk.END,
                        '     -----------------------------------------Hello，welcome to video downloader'
                        '-----------------------------------------\n')

        # 设置网格布局自动调整
        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(7):
            self.root.grid_columnconfigure(i, weight=1)

    # 视频地址输入
    def url_input(self):
        self.url.set(self.url.get().replace('&', '"&"'))  # URL中&不可用于shell（现暂时不用）

    # 选择视频保存路径
    def select_path(self):
        """Manually specify the video save destination"""
        path = filedialog.askdirectory(title='请选择一个目录')
        if path:
            self.path.set(path)

    # 打印选择的视频格式（品质）
    def select_format(self):
        """Manually select audio and video formats"""
        video_format = self.video_format.get()
        audio_format = self.audio_format.get()
        quality = video_format if not audio_format else audio_format if not video_format else video_format + '+' + audio_format
        # 日志中显示所选格式
        self.log.insert(tk.END, f'已选择音视频格式：{quality}\n')

    def print_info(self):
        """Use a thread to print video information to avoid window jamming."""
        thread = threading.Thread(target=self.get_info)
        thread.start()

    def get_info(self):
        """Display the video format information in a new window"""
        info_window = tk.Toplevel(self.root)
        info_window.geometry('1300x700')
        info_window.config(background='#CCCCFF')
        info_window.title('该视频的详细信息')

        info_txt = tk.Text(info_window, bg='#CCCCFF', fg='#000000', font=("Roboto", 12), wrap='word')
        info_txt.place(relx=0, y=0, relheight=1, relwidth=1)
        info_txt.insert(tk.END, '正在获取该视频的格式信息...\n')

        url = self.url.get()
        try:
            video_info = get_video_formats(url)
            info_txt.insert(tk.END, video_info)
            # 动态设置窗口大小
            # lines = video_info.count('\n') + 1
            # char_width = 100  # 假设每行平均字符数
            # line_height = 20  # 每行高度（像素）
            # width = min(1200, char_width * 10)  # 最大宽度 1000 像素
            # height = min(800, lines * line_height + 20)  # 最大高度 600 像素
            # info_window.geometry(f'{width}x{height}')
        except Exception as e:
            info_txt.insert(tk.END, f"获取视频信息时出错: {e}")

    def start_download(self):
        """Start video download thread"""
        self.log.insert(tk.END, '开始下载...\n')
        thread = threading.Thread(target=self.download_thread)
        thread.start()

    def download_thread(self):
        """Video download function."""
        try:
            video_format = self.video_format.get()
            audio_format = self.audio_format.get()
            # 检查是否有输入，如果有输入则添加到列表中
            quality = audio_format if not video_format else video_format if not audio_format else video_format + '+' + audio_format
            quality = "".join(quality)

            download_opts = {
                # See 'readme.md' to set more parameters you need.
                # 代理
                # 'proxy': '127.0.0.1:8889',
                # 格式
                'format': quality,
                # 视频保存路径
                'paths': {'home': self.path.get()},
                # 获取浏览器cookies，你登录相应视频网站的浏览器，你要有VIP，浏览器完全关闭
                'cookiesfrombrowser': ('edge', ),
                # 已知错误重试次数
                'extractor_retries': 10,
                # 不打印警告
                'no_warnings': True,
                # 不在下载/后处理错误时停止
                'ignoreerrors': 'only_download',
                # 等待流可用，重试时间范围
                'wait_for_video': (20, 30),
                # 下载重试次数
                'retries': 15,
                # 片段下载重复次数
                'fragment_retries': 10,
                # 文件访问重试次数
                'file_access_retries': 10,
                # 是否继续未完成的下载
                'continuedl': True,
                # 不打印进度条。
                'noprogress': False,
                # 记录消息到logging.Logger实例
                'logger': MyLogger(self.log),
            }

            with yt_dlp.YoutubeDL(download_opts) as ydl:
                ydl.download([self.url.get()])

            self.log.insert(tk.END, '下载完成。\n')
        except Exception as e:
            self.log.insert(tk.END, f'下载出现错误：{str(e)}\n')
