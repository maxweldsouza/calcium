#!/usr/bin/env python
import shutil
import os.path
from calcium import Calcium

msg = """ Pull all files in a directory outside
the folder. Can take multiple directories"""

calcium = Calcium()
args = calcium.start(msg)

for path in args:
    if not os.path.isdir(path):
        raise Exception('Not a directory')

    dirpath = os.listdir(path)
    destination = os.getcwd()
    for file in dirpath:
        filepath = os.path.join(path, file)
        print destination
        if not calcium.debug:
            shutil.move(filepath, destination)
    if not calcium.debug:
        os.rmdir(path)
