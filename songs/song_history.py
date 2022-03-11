import time
from typing import Union

from common.config import get_json_config
from common.seasideapi import SeasideAPI
from logs.thread_logger import ServiceLogger
from stream.twitch import TwitchStream

logger = ServiceLogger('song-history')


def read_song_file(config: dict):
    f = open(config.get('song_file'))
    file_song = f.readline().strip()
    f.close()

    return file_song


def run():
    config = get_json_config()
    logger.info('🎵 Starting song history logger')
    stream = TwitchStream()
    api = SeasideAPI()

    while True:
        if stream.is_live() or config.get('debug'):
            logger.info('Polling song file')

            current_song = api.get_current_song()
            file_song = read_song_file(config)
            if current_song != file_song:
                api.add_song_to_history(file_song)

        else:
            logger.info('Stream is not live, skipping poll')

        time.sleep(10)
