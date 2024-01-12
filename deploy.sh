#!/bin/bash

clear

tag_flavor=$1
tag_color=$2

# submodules
git submodule update --init --recursive --remote

## latest *psycopg2*
#echo "..... awslambda-psycopg2"
#cd ../awslambda-psycopg2
#git pull
#cd -

mkdir psycopg2
cp ../awslambda-psycopg2/psycopg2-3.8/*.py psycopg2/.
cp ../awslambda-psycopg2/psycopg2-3.8/*.so psycopg2/.

# rename files
echo "..... rename-files"
bash ./publish--rename-files.sh $tag_flavor $tag_color

# deploy
serverless deploy --stage $tag_flavor

# undo rename files
bash ./publish--undo-rename-files.sh
rm -rf psycopg2
