# Random Video Clip Generator (Docker - Windows host - Git Bash)
Plays random sections of videos for background visual noise. Great for parties.

You will need:
* Docker desktop (for Windows 10+).
* VLC.
* Git Bash.
* The videos have to be locally available.

### How to use: ###
1. Install docker: https://docs.docker.com/desktop/windows/install/
2. Install VLC (video player): https://www.videolan.org/vlc/download-windows.wa.html
3. Install git bash: https://git-scm.com/download/win
4. Create a directory here called share and download a couple of music videos there.
5. Start docker desktop and verify it's running:  
    `docker info`
6. Get image and run container (pulls and starts. These ARE the files from Windows, not copies):  
    `winpty docker run -it --name randomvideoclipgenerator_cont --volume C:\\Random-Video-Clip-Generator-Docker\\share:/root/RandomVideos/share marq4/random-video-clip-generator:latest`
7. Inside the container do (and follow those instructions):  
    `cat Instructions.txt`
8. Move the playlist file out of the share directory (in Windows).
9. Double-click the playlist file to open it with VLC.
10. To finish with the container simply:  
    `exit`
11. To log into the container after it has been stopped do:  
    `docker start randomvideoclipgenerator_cont`  
    `winpty docker exec -it randomvideoclipgenerator_cont bash`
12. To make new videos available to the container simply move them into share directory in Windows. No need to restart the container.

### Sanitize video file names: ###
[See: Clean the video file names](https://github.com/marq4/Random-Video-Clip-Generator "See: Clean the video file names")
