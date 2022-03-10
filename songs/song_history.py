import time
from typing import Union

from common.config import get_json_config
from logs.thread_logger import ServiceLogger
from stream.twitch import TwitchStream

logger = ServiceLogger('song-history')

current_song: Union[str, None] = None


def read_song_file(config: dict):
    global current_song
    f = open(config.get('song_file'))
    file_song = f.readline().strip()
    f.close()

    return file_song


def run():
    global current_song
    config = get_json_config()
    logger.info('🎵 Starting song history logger')
    stream = TwitchStream()

    while True:
        if stream.is_live() or config.get('debug'):
            logger.info('Polling song file')

            file_song = read_song_file(config)
            if current_song != file_song:
                logger.info("Got new song, adding to history")
                current_song = file_song

        else:
            logger.info('Stream is not live, skipping poll')

        time.sleep(10)
