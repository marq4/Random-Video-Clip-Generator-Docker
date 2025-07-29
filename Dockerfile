FROM ubuntu:latest

RUN mkdir -p /root/RandomVideos/share/
WORKDIR /root/RandomVideos/

ADD generate_playlist.py .
