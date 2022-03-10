from logs.thread_logger import ThreadLogger

logger = ThreadLogger('heat-level')


def run():
    logger.log('🔥 Running heat level checker')
