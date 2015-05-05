#!/usr/bin/env python
import os
import datetime
import calcium

""" Find and replace in file names
    arg1 = string to find
    arg2 = string to replace
    remainingargs = list of filenames"""

args = calcium.get_arguments()

filelist = args

for original in filelist:
    path, file = os.path.split(original)
    destination = os.path.join(path, file.lower())
    print destination
#os.rename(original, destination)
