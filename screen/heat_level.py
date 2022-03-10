from logs.thread_logger import ThreadLogger

t_logger = ThreadLogger('heat-level')


def run():
    t_logger.info('🔥 Starting heat level checker')
