# -*- coding = utf-8 -*-
# @TIME : 2024/07/08 18:30
# @Author : Grace
# @File : logger.py
# @Software : PyCharm
# Overview： Print information while downloading.

import tkinter as tk


class MyLogger:
    """A class used to show log information while downloading."""
    def __init__(self, log):
        self.log = log

    def debug(self, msg):
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)
            self.log.insert(tk.END, msg + '\n')
            self.log.see(tk.END)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        self.log.insert(tk.END, f'错误：{msg}\n')
