# Random Video Clip Generator - Docker
Plays random sections of videos for background visual noise. Great for parties. You only need to install Docker! 

You will need:
* Docker (available for Windows, Mac, & Linux).
* The videos have to be locally available.

### How to use: ###
1. Install Docker desktop: https://docs.docker.com/get-started/introduction/get-docker-desktop/ 
2. Create a directory under your C drive called share and download a couple of music videos there. For obvious reasons I cannot tell you how to download YouTube videos here. For instructions please contact me: juancmarquina@gmail.com 
3. Start docker desktop. 
4. %%% GUI %%% Get Docker Image and run it:
5. Open your web browser (like FireFox or Brave) and go to http://localhost:8000
6. IF you don't see your video clips playing, please contact me. 



8. Get image and run container (pulls and starts. The videos you see inside the container ARE the files from Windows, not copies): `winpty docker run -it --name randomvideoclipgenerator_cont --volume C:\\share:/root/RandomVideos/share marq4/random_videoclip_generator_docker:latest`
9. Inside the container do (and follow those instructions):  
    `cat instructions.txt`
10. Double-click the playlist file to open it with VLC.
11. To finish with the container simply:  
    `exit`
12. To log into the container after it has been stopped do:  
    `docker start randomvideoclipgenerator_cont`  
    `winpty docker exec -it randomvideoclipgenerator_cont bash`
13. To make new videos available to the container simply move them into share directory in Windows. No need to restart the container.

### List of suggested videos: ###
[List](https://github.com/marq4/Random-Video-Clip-Generator/blob/main/List.md "List")
