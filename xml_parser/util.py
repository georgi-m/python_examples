import argparse
import logging
import logging.config

### Parse command-line arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-i', action='store', dest='ini_file',
                help='Set path to the ini file.', required=True)
results = parser.parse_args()

logging.config.fileConfig(results.ini_file)
logger = logging.getLogger()
#logger.debug('often makes a very good meal of %s', 'visiting tourists')
#logger.info('info loggin is working %s', 'visiting tourists')

