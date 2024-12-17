"""
download.py
Provides functions for downloading videos
"""

from pytubefix import YouTube

def printProgressBar(bytes_left: int, bytes_total: int):
    percent_complete = (bytes_left/bytes_total) * 100

"""
Downloads a video from a URL
Params:
    url:                a URL leading to a youtube video
    path                Path to the directory to put the downloaded file in. If none is selected, defaults to the current working directory        
    res:                Video resolution to download. If none is selected, the highest available is used
    extension:          File extension of the video file. Defaults to 'mp4'
    onCompleteCallback: Function to call when the download is complete
    onProgressCallback: Function to call when download progress is recieved
"""
def downloadVideo(url: str, path: str = None, res: str = None, extension: str = 'mp4', on_complete_callback = None, on_progress_callback = printProgressBar):
    yt = YouTube(
        url,
        on_complete_callback=on_complete_callback,
        on_progress_callback=on_progress_callback
    )
    stream = yt.streams.filter(file_extension=extension, adaptive=True, res=None).order_by('resolution').desc.first()
    stream.download(output_path = path)