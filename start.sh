#!/bin/bash
cd ~/arcadetogo-main
source myvenv/bin/activate

export DISPLAY=:0
echo "Killing previous instances"
killall python3
killall -9 python3

echo "Start GUI"
python3 main.py
