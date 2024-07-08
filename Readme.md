# 项目简介

## yt-dlp




# 环境（使用anaconda）
1. 为项目新建conda虚拟环境,示例：conda create -n videodownload  python=3.12 
2. yt-dlp可能需要使用pip安装，进入虚拟环境：conda activate videodownload；使用pip而不是
conda安装：pip install yt-dlp

# 使用

打包

```python
# 打包命令示例，安装pyinstaller，路径自己更改
# pyinstaller -F --paths=C:\Users\14134\.conda\envs\ytdlp\Lib\site-packages --python=C:\Users\14134\.conda\envs\ytdlp\pythonw.exe  --noconsole  --icon=1.ico --name=Downloader DLP_GUI_Perfect.py
```


# 其他