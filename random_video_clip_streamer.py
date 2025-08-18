""" Live stream of random content from FFmpeg to HTTP. """

import os
import random
import subprocess
import sys
from time import sleep

PATH='/root/RandomVideos'
SUBFOLDER = 'share'
CONCAT_FILE = 'concat.txt'
NUM_CLIPS_AHEAD = 10
CLIP_LENGTH = 6
PADDING = 5
MIN_CLIP_LENGTH = 4
MAX_CLIP_LENGTH = 25


def get_random_clip_entry(video: str) -> str:
    """ Returns file VIDEO, inpoint, outpoint. """
    duration = get_video_duration(video)
    if duration <= CLIP_LENGTH + PADDING:
        start = 0
    else:
        start = random.randint(0, int(duration - CLIP_LENGTH-1))
    entry = f"file '{PATH}/{SUBFOLDER}/{video}' \n"
    entry += f"inpoint {start} \n"
    entry += f"outpoint {start + CLIP_LENGTH} \n"
    return entry
#

def refresh_concat():
    """ Build a concat playlist file with random video segments. """
    videos = get_list_of_videos()
    with open(CONCAT_FILE, 'w') as file:
        for num_clip in range(NUM_CLIPS_AHEAD):
            video = random.choice(videos)
            file.write(get_random_clip_entry(video))
            if num_clip != NUM_CLIPS_AHEAD-1:
                file.write("\n")
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
    video = f"{SUBFOLDER}/{video}"
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', \
            'v:0', '-show_entries', 'stream=duration', '-of', \
            'default=noprint_wrappers=1:nokey=1', video], capture_output=True, 
            check=False)
    duration = float(result.stdout)
    seconds = int(duration)
    # assert min_interval < seconds > 0, f"Video too short: {video} "
    return seconds
#

def try_to_accept_user_clip_length() -> None:
    """ Set global CLIP_LENGTH to what user wants or 1 - MAX. """
    global CLIP_LENGTH
    try:
        user_desire = sys.argv[1]
        CLIP_LENGTH = int(user_desire)
    except (ValueError, IndexError):
        pass
    if CLIP_LENGTH < MIN_CLIP_LENGTH:
        CLIP_LENGTH = MIN_CLIP_LENGTH
    if CLIP_LENGTH > MAX_CLIP_LENGTH:
        CLIP_LENGTH = MAX_CLIP_LENGTH
#

def main() -> None:
    """
    * Run forever:
        + Keep FFmpeg alive.
        + Stream as HSL.
        + Refresh halfway through.
    """
    try_to_accept_user_clip_length()
    while True:
        refresh_concat()
        sleep(CLIP_LENGTH * (NUM_CLIPS_AHEAD // 2))
#

if __name__ == '__main__':
    main()

