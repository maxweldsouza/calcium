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

if len(args) < 3:
    raise Exception('Incorrect no of arguments')
else:
    findstr = args[0]
    repstr = args[1]
    filelist = args[2:]

for original in filelist:
    path, file = os.path.split(original)
    destination = os.path.join(path, file.replace(findstr, repstr))
    print destination
if not calcium.debug:
    os.rename(original, destination)
