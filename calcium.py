import sys

def get_arguments():
    args = sys.argv[1:]
    piped = []
    if not sys.stdin.isatty():
        for line in sys.stdin:
            piped.append(line[:-1])

    combined = args + piped

    if not combined:
        raise Exception('No arguments given')
    return combined
