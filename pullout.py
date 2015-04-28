#!/usr/bin/env python
import shutil
import os.path
import sys
import datetime

args = sys.argv[1:]
if not args:
    print """
    Pulls out the contents of a directory
    and then deletes the directory

    Usage: pullout.py directorypath
    """
    exit()

path = args[0]
if not os.path.isdir(path):
    raise Exception('Not a directory')

dirpath = os.listdir(path)
destination = os.getcwd()
for file in dirpath:
    filepath = os.path.join(path, file)
    shutil.move(filepath, destination)
os.rmdir(path)
