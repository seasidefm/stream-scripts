import requests

from common.config import get_json_config
from logs.thread_logger import ServiceLogger

logger = ServiceLogger('seaside-api')


class SeasideAPI:
    def __init__(self):
        config = get_json_config()
        logger.info("Initializing API service")
        self.token = config.get('seaside_api_token')

    def get_current_song(self) -> str:
        response = requests.get("api.seaside.fm/songs/current", headers={
            'Authorization': self.token
        }).json()

        song_dict = response.get('data')

        return f"{song_dict.get('artist')} - {song_dict.get('song')}"


