FROM ubuntu:latest

RUN mkdir -p /root/RandomVideos/share/

ADD index.html /var/www/html/
ADD cors_server.py /var/www/html/

WORKDIR /root/RandomVideos/
ADD random_video_clip_streamer.py .
ADD stream.sh .

CMD ["/stream.sh"]
