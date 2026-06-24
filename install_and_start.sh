#!/bin/sh
cd ~/arcadetogo-main
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt

export DISPLAY=:0
python3 main.py
