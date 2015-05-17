#!/usr/bin/env python
import os
import datetime
from calcium import Calcium

msg = """ Takes a file as input and renames it with
the current date and time You can specify the
date and time format as a command line parameter """

calcium = Calcium()
args = calcium.start(msg)

format = '%d-%m-%Y'
today = datetime.date.today()

for source in args:
    filename, ext = os.path.splitext(source)
    destination = filename + today.strftime(format) + ext
    print destination
    if not calcium.debug:
        os.rename(source, destination)
