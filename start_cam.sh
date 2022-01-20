#! /bin/bash

python3 ./birdcam.py &
python3 ./file_watcher.py &

ps -aux | grep python