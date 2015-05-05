#!/usr/bin/env python
import os
import datetime
from calcium import Calcium

msg = """ Find and replace in file names
    arg1 = string to find
    arg2 = string to replace
    remainingargs = list of filenames"""

calcium = Calcium()
args = calcium.start(msg)

filelist = args

for original in filelist:
    path, file = os.path.split(original)
    destination = os.path.join(path, file.upper())
    print destination
if not calcium.debug:
    print destination
    os.rename(original, destination)
