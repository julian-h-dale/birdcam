#! /bin/bash

hug -f birdcamserver.py &
python3 ./file_watcher.py &

ps -aux | grep python