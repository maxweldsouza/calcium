#!/usr/bin/env python
import os
from calcium import Calcium

msg = """Sorts given filenames in alphabetical order"""

calcium = Calcium()
args = calcium.start(msg)

filelist = args

files = []
paths = []
for original in filelist:
    path, file = os.path.split(original)
    files.append(file)
    paths.append(path)
files.sort()
if not calcium.debug:
    for file in files:
        print path + file
