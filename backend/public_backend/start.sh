#!/bin/bash

screen -S 111forecast_public_backend -d -m bash -c 'conda run --live-stream -n 111forecast python app.py'
