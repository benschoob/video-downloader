# Command line interface to downloadVideo() in download.py
# Powershell Script version of 'ytdl' for running on windows

# Get Flags
param(
    [Parameter(Mandatory=$true)][string]$url,
    [string]$path = "None",
    [string]$res = "None",
    [string]$extension = "mp4"
)

if ($path -ne "None") { $path="'$path'" }
if ($res -ne "None") { $res="'$res'" }

# Sets the working directory to the directory this script is in
$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
cd $dir

.\venv\Scripts\activate.ps1  # Activate the python venv
python -c "from src import download; download.downloadVideo('$url', path=$path, res=$res, extension='$extension')"
deactivate
