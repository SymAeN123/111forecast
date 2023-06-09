#!/bin/bash

ROOT_DIR=$(pwd)

./kill.sh

echo "Starting servers..."
cd "${ROOT_DIR}/backend/database_api/"
screen -S 111forecast_database_api -d -m bash -c 'conda run --live-stream -n 111forecast python app.py'
cd $ROOT_DIR

cd "${ROOT_DIR}/discord/"
screen -S 111forecast_discord -d -m bash -c 'conda run --live-stream -n 111forecast python app.py'
cd $ROOT_DIR

cd "${ROOT_DIR}/backend/public_backend/"
screen -S 111forecast_public_backend -d -m bash -c 'conda run --live-stream -n 111forecast python app.py'
cd $ROOT_DIR
echo -e "Servers started. Use \"screen -ls\" to view and \"screen -r {sessionname}\" to enter server sessions."
