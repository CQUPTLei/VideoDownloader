import tkinter as tk

width = 900
height = 500


class App:
    def __init__(self):
        self.root = tk.Tk()
        screenwidth = self.root.winfo_screenwidth()  # 获取显示器分辨率
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 4)
        # Set geometry to NEWGEOMETRY of the form = widthxheight+x+y.
        self.root.geometry(size)
        self.root.update()
        self.root.title("VideoDownloader")

        # 创建变量
        self.url = tk.StringVar()
        self.path = tk.StringVar()
        self.video_format = tk.StringVar()
        self.audio_format = tk.StringVar()

        # 输入视频URL部分
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

        path_button = tk.Button(self.root, text='Select the path to save the video', bg='#C1CDC1', command=self.select_path)
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

        dl_button = tk.Button(self.root, text='Start  download', bg='#008B00', font=('Impact', 13), command=self.start_download)
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

    def url_input(self):
        pass

    def print_info(self):
        pass

    def select_path(self):
        pass

    def select_format(self):
        pass

    def start_download(self):
        pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
