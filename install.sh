#!/bin/bash
echo "Install and prepare venv"
cd ~/arcadetogo-main
python3 -m venv myvenv
source myvenv/bin/activate
pip3 install -r requirements.txt