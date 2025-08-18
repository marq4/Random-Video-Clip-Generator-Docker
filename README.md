# Random Video Clip Streamer - Docker
Play random sections of videos for background visual noise. Great for parties. You only need to install Docker! 

You will need:
* Docker Desktop (available for Windows and Linux).
* The videos have to be previously downloaded locally.

### How to use: ###
1. Install Docker Desktop: https://docs.docker.com/get-started/introduction/get-docker-desktop/ 
2. Create a directory under your C drive called 'share' and download a couple of music videos there. For obvious reasons I cannot tell you how to download YouTube videos here. For instructions please contact me: juancmarquina@gmail.com 
3. Start Docker Desktop. 
4. Open the Docker Desktop GUI.
   i. Go to Docker Hub section on the right vertical menu.
   ii. Search for and select "marq4/random_video_clip_streamer".
   iii. Click "pull" button.
   iv. Go to Images section. Select the image you just downloaded. Click the play button. Expand Optional Settings. Give your container a name, e.g. RandomVideoClipStreamerContainer (optional). 
   To specify a clip duration pass this enviornment variable: USER_CLIP_LENGTH. The valid range is between 3 and 25 seconds but the default and recommeneded minimun value is 6.
6. Open your web browser (like FireFox or Brave) and go to http://localhost:8080
7. Reload the web browser as needed and wait for a couple of seconds.
8. IF you don't see your video clips playing, please contact me.
9. To make new videos available to the container simply move them into share directory in your host OS (e.g. Windows), no need to restart the container. 

### List of suggested videos: ###
[List](https://github.com/marq4/Random-Video-Clip-Generator/blob/main/List.md "List")
