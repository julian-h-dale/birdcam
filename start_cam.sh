#! /bin/bash

hug -f birdcamserver.py &
sleep 2
python3 ./sensor_client.py &
python3 ./file_watcher.py &

ps -aux | grep python