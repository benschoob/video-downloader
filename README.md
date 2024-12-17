# ytdl

A simple youtube video downloader with GUI and CLI options /
THIS PROJECT IS UNDER DEVELOPMENT. The code here is not stable and probably doesn't work.

## Setup

### Step 1: Installing Python

First, make sure you have python installed. You can find installations here: https://www.python.org/downloads

### Step 2: Setting up the venv

Next, you'll need to run the venv setup script. This creates a virtual python environment that includes all of the required libraries.
```bash
./venv_setup.sh
```
(NOTE: you may need to give this script execution permissions. You can do this by running `chmod +x ./venv_setup.sh`)

## Using the CLI

To download a video from the command line, run the script `ytdl` (You may need to give it execution permissions):
```bash
./ytdl [-p path | -r resolution | -e extension] <url>
```
This downloads a youtube video from a youtube URL. The downloaded video file will be in the directory indicated by the `path` flag. If this flag is not set, the video file will be put in the 'ytdl' directory. The `resolution` flag sets the desired video resolution. If not set, this defaults to the highest available resolution. The `extension` flag sets the file extension for the downloaded file. If not set, this defaults to 'mp4'. 

## Using the GUI

The GUI is currently under development and does not exist. Come back later.