# Random Video Clip Generator (Docker - Windows host - Git Bash)
Plays random sections of videos for background visual noise. Great for parties.

You will need:
* Docker desktop (for Windows 10).
* VLC.
* Git Bash.
* The videos have to be locally available.

### How to use: ###
1. Install docker: https://docs.docker.com/desktop/windows/install/
2. Install VLC (video player): https://www.videolan.org/vlc/download-windows.wa.html
3. Install git bash: https://git-scm.com/download/win
4. Create a directory under your C drive called share and download a couple of music videos there.
5. Start docker desktop and verify it's running:
    `docker info`
6. Get image and run container (pulls and starts. The videos you see inside the container ARE the files from Windows, not copies):  
    `winpty docker run -it --name randomvideoclipgenerator_cont --volume C:\\share:/root/RandomVideos/share marq4/random-video-clip-generator:latest`
7. Inside the container do (and follow those instructions):  
    `cat Instructions.txt`
8. Double-click the playlist file to open it with VLC.
9. To finish with the container simply:  
    `exit`
10. To log into the container after it has been stopped do:  
    `docker start randomvideoclipgenerator_cont`  
    `winpty docker exec -it randomvideoclipgenerator_cont bash`
11. To make new videos available to the container simply move them into share directory in Windows. No need to restart the container.

### List of suggested videos: ###
[List](https://github.com/marq4/Random-Video-Clip-Generator/blob/main/List.md "List")
