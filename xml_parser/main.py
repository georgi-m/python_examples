import argparse

### Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-l', action='store', dest='log_level',
                help='Setting log level.')
