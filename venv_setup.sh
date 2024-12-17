#!/bin/bash

# Sets up a python virtual environment for running the python script

python -m venv ./venv
source ./venv/bin/activate

# Install python packages
pip install pytubefix

deactivate