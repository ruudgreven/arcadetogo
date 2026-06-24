#!/bin/sh
echo "Install and prepare venv"
cd ~/arcadetogo-main
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt

export DISPLAY=:0
echo "Killing previous instances"
killall python3
killall -9 python3

echo "Start GUI"
python3 main.py
