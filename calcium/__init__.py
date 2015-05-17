import sys

class Calcium:
    debug = False
    def start(self, msg):
        args = sys.argv[1:]
        piped = []
        if not sys.stdin.isatty():
            for line in sys.stdin:
                piped.append(line[:-1])

        combined = args + piped

        if not combined:
            print msg
            raise Exception('No arguments given')
        if combined[0] == 'debug':
            self.debug = True
            combined = combined[1:]
        return combined
