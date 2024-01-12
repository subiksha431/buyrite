#!/bin/bash

cd ./buyrite/utils
pwd

tag_flavor=$1
tag_color=$2
cp config.$tag_flavor.$tag_color.p# config.py

#cat config.py
sleep 7

cd -
pwd
