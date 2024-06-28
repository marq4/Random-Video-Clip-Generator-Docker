FROM ubuntu:latest

RUN mkdir -p /root/RandomVideos/share/
WORKDIR /root/RandomVideos/

ADD Instructions.txt .
ADD random_clip_generator.py .
ADD sanitize_video_titles.py .
