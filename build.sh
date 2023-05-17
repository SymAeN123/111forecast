#!/bin/bash

if ! command -v npm &> /dev/null
then
    echo -e "Need to install node.js"
    echo -e "You can install it by following the instructions in README.md"
    exit
fi

ROOT_DIR=$(pwd)

cd "${ROOT_DIR}/frontend/"
npm run build
cd $ROOT_DIR