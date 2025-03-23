#!/bin/bash
# link to guide https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-20-04
# get required tools
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools

#setup virual enviroment
sudo apt install python3-venv

#ensure that this runs in the correct folder
python3 -m venv GameStorageEnv
source GameStorageEnv/bin/activate

pip install wheel
pip install uwsgi flask
pip install requests
#Change ufw to allow access to port 5000
sudo ufw allow 5000
#You should be able to run GameStorageNode now - ensure that it runs on the correct port