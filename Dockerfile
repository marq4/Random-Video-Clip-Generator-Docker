FROM ubuntu:latest

RUN mkdir -p /root/RandomVideos/share/
WORKDIR /root/RandomVideos/

ADD install_programs.sh .
ADD Instructions.txt .
ADD random_clip_generator.py .
ADD sanitize_video_titles.py .

RUN chmod +x install_programs.sh
