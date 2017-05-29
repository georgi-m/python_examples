import argparse

### Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='ini_file',
                help='Set path to the ini file.', required=True)
results = parser.parse_args()
