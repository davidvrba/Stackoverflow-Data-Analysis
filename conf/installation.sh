#!/bin/bash

apt-get update
apt --assume-yes install python3-pip
pip3 install jupyter
pip3 install boto3
pip3 install requests
apt-get install p7zip-full
mkdir data
cd src
python3 data_download.py 
jupyter notebook --nobrowser --port=8888