import argparse
import logging

### Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-l', action='store', dest='log_level',
                help='Setting log level.')
results = parser.parse_args()

### Setting log level.
LEVELS = { 'debug':logging.DEBUG,
           'info':logging.INFO,
           'warning':logging.WARNING,
           'error':logging.ERROR,
           }
level = LEVELS.get(results.log_level, logging.NOTSET)
logging.basicConfig(filename='example.log',
                    level=level
                    )
log_example = logging.getLogger('example')
