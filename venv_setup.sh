#!/bin/bash

# Sets up a python virtual environment for running the python script

python -m venv ./venv
source ./venv/bin/activate
pip install pytubefix
deactivate