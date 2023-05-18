#!/bin/bash

ROOT_DIR=$(pwd)

if ! command -v conda &> /dev/null
then
    echo "Anaconda/Miniconda is not installed!"
    echo -e "You can install miniconda from \e]8;;https://docs.conda.io/en/latest/miniconda.html\ahere\e]8;;\a."
    exit
fi

if ! command -v screen &> /dev/null
then
    echo -e "Need to install \"screen\""
    echo -e "You can install it by running \"sudo apt install screen\""
    exit
fi

if conda info --envs | grep -q 111forecast 
then 
    echo "Conda env 111forecast already exists"
else
    echo "Creating conda env 111forecast"
    conda env create -f environment.yml
fi

echo "Initializing database:"
cd "${ROOT_DIR}/backend/database_api/"
mkdir contests
conda run --live-stream -n 111forecast python init.py
cd $ROOT_DIR
echo "Database initialized."

if ! command -v npm &> /dev/null
then
    echo -e "Didn't detect installation of npm."
    echo -e "This is okay if you are planning to run the website on a localhost, but if you are planning to deploy, you will need to change the proxy server in ./frontend/vite.config.js to the exposed url on your deployment server, then run the build script. This script requires npm."
    echo -e "You can install it by following the instructions in README.md"
fi
