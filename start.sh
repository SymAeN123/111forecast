#!/bin/bash

ROOT_DIR=$(pwd)

cd "${ROOT_DIR}/backend/public_backend/"
./start.sh
cd $ROOT_DIR

touch success.txt