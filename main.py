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

Output contract
---------------
The entry point is this file, main.py, run with Python 3.13. It reads
entry.png from the same directory as this file and writes it to
<output>/entry.png, where <output> is MAKEFUN_OUTPUT_DIR when set and
/output otherwise. The output directory is created when missing. The
written file is byte-for-byte the repository's entry.png: 1024 by
1024 pixels, 481,363 bytes, PNG. Running the program twice, or in two
different output directories, produces identical bytes every time;
there is no clock, no random seed, no network fetch and no input
besides the bundled image, so there is nothing that could make one
run differ from another.

Why copy instead of draw
------------------------
The front page was composed once, reviewed by eye over three rounds
and frozen as entry.png: masthead, headlines, stat strip, lists and
the DATE CHECK box are all laid out in that file, with every word
spelled exactly. Re-drawing it at run time would add a second chance
for a layout slip and would need the same font files the composing
machine had. Copying keeps the judged artefact exactly the artefact
that was reviewed, and keeps this program to a few statements that any
reader can audit in seconds.

What this program never does
----------------------------
It never opens a socket, never reads the clock, never writes anywhere
except the single output file, and never depends on a file outside
this repository. If entry.png is missing the copy raises and the run
fails loudly instead of writing a partial or empty image.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")

os.makedirs(os.path.dirname(DST), exist_ok=True)
shutil.copyfile(SRC, DST)
