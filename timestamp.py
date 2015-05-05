#!/usr/bin/env python
import os
import sys
import datetime

# Takes a file as input and renames it with
# the current date and time
# You can specify the date and time format as
# a command line parameter

args = sys.argv[1:]
piped = []
if not sys.stdin.isatty():
    for line in sys.stdin:
        piped.append(line[:-1])

combined = args + piped

if not combined:
    raise Exception('No arguments given')

format = '%d-%m-%Y'
today = datetime.date.today()

for source in combined:
    filename, ext = os.path.splitext(source)
    destination = filename + today.strftime(format) + ext
    print destination
#os.rename(source, destination)
