#!/usr/bin/env python
import os
import calcium

""" Sorts given filenames in alphabetical order"""

args = calcium.get_arguments()

filelist = args

files = []
paths = []
for original in filelist:
    path, file = os.path.split(original)
    files.append(file)
    paths.append(path)
files.sort()
for file in files:
    print path + file
