import logging
logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.warning('This is a warning')
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')