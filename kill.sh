#!/bin/bash

echo "Attempting to kill servers if they exist:"
screen -X -S 111forecast_public_backend quit
screen -X -S 111forecast_discord quit
screen -X -S 111forecast_database_api quit
