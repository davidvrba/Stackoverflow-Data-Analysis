#!/bin/bash

apt-get update
apt --assume-yes install python3-pip
pip3 install jupyter
pip3 install boto3
pip3 install requests
apt-get install p7zip-full
mkdir data
python3 Stackoverflow-Data-Analysis/src/data_download.py
7z x /home/ubuntu/data/posts.7z
