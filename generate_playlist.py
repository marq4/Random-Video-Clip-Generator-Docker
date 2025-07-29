#! /usr/bin/env python

""" Random Video Clip Generator - Docker. """

import os
import random
import subprocess
import sys
import xml.etree.ElementTree as ET
from subprocess import Popen


XML_PLAYLIST_FILE = 'clips.xspf'
SUBFOLDER = 'share'
DEFAULT_NUM_CLIPS = 10_000
DEFAULT_INTERVAL_MIN = 2
DEFAULT_INTERVAL_MAX = 4


def verify_intervals_valid(min_interval: int, max_interval: int) -> None:
    """
    * Video clips must be between 1 to 25 seconds long.
    * The highest min interval is 15. 
    * The highest max interval is 25. 
    """
    assert 15 >= min_interval >= 1
    assert 25 >= max_interval >= 1
#

def generate_random_video_clips_playlist(
        video_list: list,
        number_of_clips: int,
        min_interval: int,
        max_interval: int) -> ET.Element:
    """
    * Create playlist as an xml element tree.
    * Create tracklist as subelement of playlist. This contains the clips.
    * For each clip to be generated:
        + Select a video at random.
        + Choose beginning and end of clip from selected video.
        + Add clip to playlist.
    """
    assert video_list and number_of_clips > 0

    playlist = ET.Element("playlist", version="1", xmlns="http://xspf.org/ns/0/")
    tracks = ET.SubElement(playlist, "trackList")

    assert 1 <= number_of_clips < sys.maxsize, \
        "Invalid number of clips: {number_of_clips} "

    for iteration in range(number_of_clips):
        video_file = select_video_at_random(video_list)
        duration = get_video_duration(iteration, video_file, min_interval)
        begin_at = choose_starting_point(duration, max_interval)
        clip_length = random.randint(min_interval, max_interval)
        play_to = begin_at + clip_length
        video_file = video_file.replace('{SUBFOLDER}/', '')
        add_clip_to_tracklist(tracks, video_file, begin_at, play_to)

    return playlist
#

def add_clip_to_tracklist(track_list: ET.Element, \
        video: str, start: int, end: int) -> None:
    """ Add clip (track) to playlist.trackList sub element tree and mute.
        :param: track_list: Contains the clips.
        :param: video: The name of the video file to be cut.
        :param: start: Begin clip from.
        :param: end: Stop clip at. """
    assert track_list is not None and video and start >= 0
    track = ET.SubElement(track_list, 'track')
    ET.SubElement(track, 'location').text = f"file:///{video}"
    extension = ET.SubElement(track, 'extension', \
        application='http://www.videolan.org/vlc/playlist/0')
    ET.SubElement(extension, 'vlc:option').text = f"start-time={start}"
    ET.SubElement(extension, 'vlc:option').text = f"stop-time={end}"
    ET.SubElement(extension, 'vlc:option').text = 'no-audio'
#

def create_xml_file(playlist_et: ET.Element) -> None:
    """ Finally write the playlist tree element as an xspf file to disk. """
    ET.ElementTree(playlist_et).write(XML_PLAYLIST_FILE)
    prepend_line(XML_PLAYLIST_FILE, '<?xml version="1.0" encoding="UTF-8"?>')
#

def choose_starting_point(video_length: int, max_interval: int) -> int:
    """ Choose beginning of clip.
    :return: Starting point from beginning of video to end of video - max. """
    assert video_length > 0
    return random.randint(0, video_length - max_interval)
#

def select_video_at_random(list_of_files: list) -> str:
    """ Choose a video. :return: Video filename with subpath only. """
    assert list_of_files and SUBFOLDER
    selected = random.randint(0, len(list_of_files) - 1)
    return f"{SUBFOLDER}/{list_of_files[selected]}"
#

def prepend_line(filename: str, line: str) -> None:
    """ Append line to beginning of file. """
    assert filename, f"Cannot prepend line: '{line}' to invalid {filename}. "
    if line is not None and len(line) > 0:
        with open(filename, 'r+', encoding='utf-8') as file:
            content = file.read()
            file.seek(0,0)
            file.write( line.rstrip("\r\n") + "\n" + content )
#

def list_files_subfolder() -> list:
    """ Create a list of all files 'share' subfolder. """
    subfolder_contents = os.listdir(SUBFOLDER)
    if subfolder_contents is None or len(subfolder_contents) < 1:
        print('There are no files under "share" subfolder.')
        print('Please download some music videos here ' + \
                '(on your host OS, e.g. Windows).')
        sys.exit()
    return subfolder_contents
#

def get_video_duration(num_to_log: int, video: str, min_interval: int) -> int:
    """ Extract video duration with ffprobe and subprocess.Popen.
        :return: Video duration in seconds. """
    assert video
    ffprobe_str = "ffprobe -v error -select_streams v:0 \
        -show_entries stream=duration -of default=noprint_wrappers=1:nokey=1"
    command = f"{ffprobe_str} {video} "
    with Popen(command, stdout=subprocess.PIPE, shell=True) as process:
        (out, err) = process.communicate()
    if err:
        print(f"Process error: [{str(err)}]. Iteration: {num_to_log}. ")
    result = ( ( ( ( str(out) ).split('.', maxsplit=1) )[0] ).split("b'") )[1]
    seconds = int(result)
    assert min_interval < seconds > 0, f"Video too short: {video} "
    return seconds
#

def remove_playlist_if_found(files: list) -> list:
    """ Remove playlist file if found under videos subdir. """
    if XML_PLAYLIST_FILE in files:
        files.remove(XML_PLAYLIST_FILE)
    return files
#


def main():
    """
    * Get values for number of clips to generate, intervals, or choose defaults. 
    * Get list of videos from 'share' subfolder.
    * Generate an xml playlist with random clips from those videos.
    * Run VLC with that playlist.
    """
    number_of_clips = sys.argv[1] or DEFAULT_NUM_CLIPS
    interval_min = sys.argv[2] or DEFAULT_INTERVAL_MIN
    interval_max = sys.argv[3] or DEFAULT_INTERVAL_MAX
    verify_intervals_valid(interval_min, interval_max)
    files = list_files_subfolder()
    files = remove_playlist_if_found(files)
    top_element = generate_random_video_clips_playlist(files, \
            number_of_clips, interval_min, interval_max)
    create_xml_file(top_element)
    print(f"VLC playlist generated: {XML_PLAYLIST_FILE}")
    subprocess.run(['vlc', f"{XML_PLAYLIST_FILE}"], check=False)
#


if __name__ == '__main__':
    main()
#
