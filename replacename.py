#!/usr/bin/env python
import os
import sys
import datetime

""" Find and replace in file names
    arg1 = string to find
    arg2 = string to replace
    remainingargs = list of filenames"""

args = sys.argv[1:]
piped = []
if not sys.stdin.isatty():
    for line in sys.stdin:
        piped.append(line[:-1])

combined = args + piped

if len(combined) < 3:
    raise Exception('Incorrect no of arguments')
else:
    findstr = combined[0]
    repstr = combined[1]
    filelist = combined[2:]

for original in filelist:
    path, file = os.path.split(original)
    destination = os.path.join(path, file.replace(findstr, repstr))
    print destination
#os.rename(original, destination)
