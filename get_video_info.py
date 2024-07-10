# -*- coding = utf-8 -*-
# @TIME : 2024/07/08 18:30
# @Author : Grace
# @File : get_video_info.py
# @Software : PyCharm
# Overview： Get video format and other related information.

import yt_dlp
from prettytable import PrettyTable
import math


def convert_bytes(size_bytes):
    """将文件大小转换为更适合阅读的单位"""
    if size_bytes is None:
        return "Unknown"
    elif size_bytes == 0:
        return "0 B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


def get_video_formats(url):
    """
    获取视频格式信息
    :param url: 视频的URL
    :return: 返回格式化的视频信息字符串
    """
    ydl_opts = {
        'quiet': True,  # 静音模式，只显示我们需要的信息
        'cookiesfrombrowser': ('edge', ),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        formats = info_dict.get('formats', [])

        # 创建表格
        table = PrettyTable()
        table.field_names = ["Format Code", "Extension", "Resolution", "Note", "File Size", "FPS", "Bitrate",
                             "Audio Codec", "Video Codec"]

        # 填充表格
        for f in formats:
            # print(f)
            # print('\n')
            table.add_row([
                f['format_id'],
                f['ext'],
                f.get('resolution', 'Unknown'),
                f.get('format', 'Unknown'),
                convert_bytes(f.get('filesize_approx')),
                f.get('fps', 'Unknown'),
                f.get('tbr', 'Unknown'),
                f.get('acodec', 'Unknown'),
                f.get('vcodec', 'Unknown')
            ])

        # 返回表格字符串
        return table.get_string()
