""" Remove spaces and special characters from file names. """

import os
import re

for original in os.listdir("share"):
    prefix = '/root/RandomVideos/share'
    if original == os.path.basename(__file__) \
        or original == 'random_clip_generator.py':
        continue
    sanitized = re.sub(r"[^a-zA-Z0-9\.]", '', original)
    if sanitized != original:
        os.rename(f"{prefix}/{original}", f"{prefix}/{sanitized}")
