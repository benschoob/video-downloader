from tkinter import *
from tkinter import ttk

from threading import Thread

from download import downloadVideo, bytesToBestSize

def downloadProgress(stream, chunk, bytes_remaining):
    percent_complete = (stream.filesize - bytes_remaining)/stream.filesize

    filename.set("Downloading '{}'. . .".format(stream.default_filename))
    progress_text.set("{}/{} ({:.1f}%)".format(bytesToBestSize(stream.filesize - bytes_remaining), bytesToBestSize(stream.filesize), percent_complete * 100))
    progress.set(percent_complete * 100)

def downloadComplete(stream, file_path):
    progress.set(100)
    filename.set("Download Complete.")

# Function called when download_button is clicked
def downloadButtonCallback():
    def download():
        link = url.get()
        downloadVideo(link, on_progress_callback=downloadProgress, on_complete_callback=downloadComplete)
    t = Thread(target=download)
    t.start()

root = Tk()
root.title("ytdl")

# Tab notebook object
tabCtrl = ttk.Notebook(root)

# Initialize notebook pages

# Downloads
download_frame = ttk.Frame(tabCtrl, padding=10)
download_frame.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

# Files
files_frame = ttk.Frame(tabCtrl, padding=10)
files_frame.grid(column=0, row=0, sticky=(N, W, E, S))

# Search
search_frame = ttk.Frame(tabCtrl, padding=10)
download_frame.grid(column=0, row=0, sticky=(N, W, E, S))

tabCtrl.add(download_frame, text="Download")
tabCtrl.add(files_frame, text="Files")
tabCtrl.add(search_frame, text="search")

# download widget
url = StringVar()
url_entry = ttk.Entry(download_frame, textvariable=url, width=50)
url_entry.grid(column=0, row=0, sticky=(W, E))

download_button = ttk.Button(download_frame, text="Download", command=downloadButtonCallback)
download_button.grid(column=0, row=1, sticky=S)

progress_frame = ttk.Frame(download_frame, padding=5)
progress_frame.grid(column=0, row=2, sticky=(W, E))

filename = StringVar()
ttk.Label(progress_frame, textvariable=filename).grid(column=0, row=0, columnspan=2, sticky=W)

progress = IntVar()
prog_bar = ttk.Progressbar(progress_frame, variable=progress)
prog_bar.grid(column=0, row=1, sticky=W)

progress_text = StringVar()
ttk.Label(progress_frame, textvariable=progress_text).grid(column=1, row=1, sticky=E)

#files widget

# search widget

# pack the bookmarks widget and start the main loop
tabCtrl.pack()
root.mainloop()