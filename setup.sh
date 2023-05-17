#!/bin/bash

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
