import argparse
import logging
import logging.config
import ConfigParser

### Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='ini_file',
                help='Set path to the ini file.', required=True)
results = parser.parse_args()

### Creating logger
logging.config.fileConfig(results.ini_file)
logger = logging.getLogger()

### Parsing ini file
config = ConfigParser.ConfigParser()
config.read(results.ini_file)
