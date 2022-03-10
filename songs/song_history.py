import time
from typing import Union

from common.config import get_json_config
from logs.thread_logger import ServiceLogger
from stream.twitch import TwitchStream

logger = ServiceLogger('song-history')

current_song: Union[str, None] = None
def read_song_file():
    global current_song


def run():
    config = get_json_config()
    logger.info('🎵 Starting song history logger')
    stream = TwitchStream()

    while True:
        if stream.is_live() or config.get('debug'):
            logger.info('Polling song file')
        else:
            logger.info('Stream is not live, skipping poll')

        time.sleep(10)
