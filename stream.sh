#! /bin/bash -

cd /var/www/html/ && python3.10 cors_server.py &

python3.10 random_video_clip_streamer.py
