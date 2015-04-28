import os
import sys
import datetime

# Takes a file as input and renames it with
# the current date and time
# You can specify the date and time format as
# a command line parameter

args = sys.argv[1:]
if not args:
    throw ('No filename given')
elif len(args) == 1:
    format = '%d-%m-%Y'
else:
    format = args[1]
today = datetime.date.today()

source = args[0]
filename, ext = os.path.splitext(source)
destination = filename + today.strftime(format) + ext
os.rename(source, destination)
