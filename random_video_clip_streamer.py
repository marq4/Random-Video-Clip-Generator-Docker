""" Pseudo-live stream of random content from FFmpeg to HTTP. """

import os
import random
import subprocess
import sys
import time

SUBFOLDER = 'share'
NUM_CLIPS = 5
CLIP_LENGTH = 4


def select_video_at_random(list_of_files: list) -> str:
    """ Choose a video. :return: Video filename with subpath only. """
    assert list_of_files and SUBFOLDER
    selected = random.choise(list_of_files)
    return selected
#

def get_list_of_videos() -> list:
    """ Returns list of video titles inside SUBFOLDER. """
    subfolder_contents = os.listdir(SUBFOLDER)
    if subfolder_contents is None or len(subfolder_contents) < 1:
        print(f"There are no files under '{SUBFOLDER}' subfolder.")
        print('Please download some music videos here ' + \
                '(on your host OS, e.g. Windows).')
        sys.exit()
    return subfolder_contents
#

def get_video_duration(video: str) -> int:
    """ Extract video duration with ffprobe and subprocess.Popen.
        :return: Video duration in seconds. """
    assert video
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', \
            'v:0', '-show_entries', 'stream=duration', '-of', \
            'default=noprint_wrappers=1:nokey=1', video], \
            capture_output=True, check=False)
    duration = float(result.stdout)
    seconds = int(duration)
    # assert min_interval < seconds > 0, f"Video too short: {video} "
    return seconds
#

def choose_starting_point(video_duration: int) -> int:
     """ Choose beginning of clip. """
     assert video_duration > 0
     return random.randint(0, video_duration - CLIP_LENGTH)
#


def main() -> None:
    """
    * Randomly select a video from SUBFOLDER and time segment.
    * Spawn FFmpeg to encode the segment into HLS.
    * Update the m3u8 playlist and segment files.
    * Repeat for NUM_CLIPS.
    """
    videos = get_list_of_videos()
    for _ in range(NUM_CLIPS):
        video = select_video_at_random(videos)
        duration = get_video_duration(video)
        begin_at = choose_starting_point(duration)
        output_path = "/var/www/html/playlist.m3u8"
        subprocess.run(["ffmpeg", "-re", "-ss", str(start), "-i", video,
            "-t", str(CLIP_LENGTH), "-c:v", "libx264", "-c:a", "aac", 
            "-f", "hls", "-hls_time", "4", "-hls_list_size", "5",
            "-hls_flags", "delete_segments", output_path])
        time.sleep(CLIP_LENGTH)
#

if __name__ == '__main__':
    main()

