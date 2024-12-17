"""
download.py
Provides functions for downloading videos
"""

from pytubefix import YouTube, Stream # type: ignore

"""
Converts a number of bytes to the appropriate units (KB, MB or GB)
"""
def bytesToBestSize(bytes: int) -> str:
    if bytes < 2**10:
        return "{} bytes".format(bytes)
    elif bytes < 2**20:
        return "{:.1f}KB".format(bytes/2**10)
    elif bytes < 2**30:
        return "{:.1f}MB".format(bytes/2**20)
    else:
        return "{:.1f}GB".format(bytes/2**30)

"""
Returns a progress bar composed of unicode characters.
"""
def progressBar(len: int, percent_complete) -> str:
    full_bars = round(len * percent_complete)
    empty_bars = len - full_bars
    
    bar = "\u2588" * full_bars + " " * empty_bars
    return bar

"""
Prints a message reporting the progress of a pytube stream download to the console
Used as the default on_progress_callback for downloadVideo()
"""
def printProgressMessage(stream, chunk, bytes_remaining):
    percent_complete = ((stream.filesize - bytes_remaining)/stream.filesize)
    print(
        "Downloading '{}' |{}| {}/{} ({:.1f}%)".format(
            stream.default_filename, 
            progressBar(20, percent_complete), 
            bytesToBestSize(stream.filesize - bytes_remaining), 
            bytesToBestSize(stream.filesize), 
            percent_complete * 100
            ),
        end='\r'
    )

"""
Prints a message reporting that a pytube stream has finished downloading
Used as the default on_complete_callback for downloadVideo()
"""
def printCompleteMessage(stream, file_path):
    print("\nDownload Complete.")

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
def downloadVideo(url: str, path: str = None, res: str = None, extension: str = 'mp4', on_complete_callback = printCompleteMessage, on_progress_callback = printProgressMessage):
    yt = YouTube(
        url,
        on_complete_callback=on_complete_callback,
        on_progress_callback=on_progress_callback
    )
    stream = yt.streams.filter(file_extension=extension, adaptive=True, res=None).order_by('resolution').desc().first()
    stream.download(output_path = path)