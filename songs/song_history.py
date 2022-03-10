import time

from logs.thread_logger import ThreadLogger

logger = ThreadLogger('song-history')


def run():
    logger.info('🎵 Starting song history logger')

    time.sleep(10)
    logger.info('Some later log')
