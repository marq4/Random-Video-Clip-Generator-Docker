FROM ubuntu:latest

RUN mkdir -p /root/RandomVideos/share/
WORKDIR /root/RandomVideos/

ADD random_clip_generator.py .
