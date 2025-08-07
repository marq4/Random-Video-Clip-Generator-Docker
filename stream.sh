#! /bin/bash -

cd /var/www/html/ && python3 cors_server.py &

python3 random_video_clip_streamer.py
