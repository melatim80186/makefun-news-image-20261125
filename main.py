"""Entry program for make.fun news-image-20261125.

Copies the pre-drawn 1024x1024 PNG in this repository to the output
directory. Standard library only, no network, deterministic: the same
bytes are written on every run.

The image itself is a one-page newspaper front page for Wednesday
25 November 2026: a generated triptych (burning cargo ship Sparta II
in the Gulf of Finland, Riyadh's tallest tower after the Houthi drone
strike, the Huawei verdict gavel) under a masthead naming the day,
plus the CIA/ODNI cyber-breach lead, three hero stories, a six-number
stat strip, ten more stories, and a red DATE CHECK box listing big
stories that are NOT from 25 November so they cannot be mistaken
for today's news. The program only copies the finished image; it
draws nothing and fetches nothing.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
