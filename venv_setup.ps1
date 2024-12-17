# Sets up a python virtual environment for running the python script
# Powershell Script version of venv_setup.sh for running on windows

python -m venv .\venv
.\venv\Scripts\activate.ps1

# Install python packages
pip install pytubefix

deactivate