#!bin/bash

#install pip
sudo apt-get install python-pip 

#upgrading the version of pip
sudo pip install -U pip 

#installing tweepy using pip. If pip is not installed than install pip first
sudo pip install tweepy

#matplotlib library installation 
sudo pip install matplotlib

#For dependency of matplotlib
sudo apt-get install libjpeg8-dev
sudo apt-get install libpng-dev
sudo apt-get install libfreetype6-dev

#installing pandas library
sudo pip install pandas