# video-downloader

A simple youtube video downloader with GUI and CLI options. Implemented using the `pytube` library (https://pypi.org/project/pytube/)

## Setup

### Step 1: Installing Python

First, make sure you have python installed. You can find installations here: https://www.python.org/downloads

### Step 2: Setting up the venv

Next, you'll need to run the venv setup script. This creates a virtual python environment that includes all of the required libraries.

#### Linux/Unix/MacOS:

```bash
./venv_setup.sh
```
(NOTE: you may need to give this script execution permissions. You can do this by running `chmod +x ./venv_setup.sh`)

#### Windows:

```powershell
.\venv_setup.ps1
```

## Using the CLI

### Linux/Unix/MacOS

To download a video from the command line, run the script `ytdl` (You may need to give it execution permissions):
```bash
./ytdl [-p path | -r resolution | -e extension] <url>
```
This downloads a youtube video from a youtube URL. The downloaded video file will be in the directory indicated by the `path` flag. If this flag is not set, the video file will be put in the 'ytdl' directory. The `resolution` flag sets the desired video resolution. If not set, this defaults to the highest available resolution. The `extension` flag sets the file extension for the downloaded file. If not set, this defaults to 'mp4'. 

### Windows

To download a video from the command line, run the script `ytdl.ps1`

```powershell
.\ytdl <url> -path <path> -res <resolution> -extension <extension>
```

This downloads a youtube video from a youtube URL. The downloaded video file will be in the directory indicated by the `path` flag. If this flag is not set, the video file will be put in the 'ytdl' directory. The `res` flag sets the desired video resolution. If not set, this defaults to the highest available resolution. The `extension` flag sets the file extension for the downloaded file. If not set, this defaults to 'mp4'.

## Using the GUI

To start the GUI, run the `ytldGUI` script on Linux/Unix/MacOS or the `ytdl.ps1` script on Windows. Once the interface opens, paste a youtube link into the text entry field and click the 'Download' button to download that video as a 1080p mp4. This file will be located in the ytld directory.

(NOTE: The GUI is currently in development and should have more features soon) 
