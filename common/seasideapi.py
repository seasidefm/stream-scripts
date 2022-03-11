import requests

from common.config import get_json_config
from logs.thread_logger import ServiceLogger

logger = ServiceLogger('seaside-api')


class SeasideAPI:
    def __init__(self):
        config = get_json_config()
        logger.info("Initializing API service")
        self.token = config.get('seaside_api_token')
        self.host = config.get('seaside_api_host') or "https://api.seaside.fm"

    def get_current_song(self) -> str:
        response = requests.get(f"{self.host}/songs/current", headers={
            'Authorization': self.token
        }).json()

        song_dict = response.get('data')

        return f"{song_dict.get('artist')} - {song_dict.get('song')}"

    def add_song_to_history(self, song: str):
        response = requests.post(f"{self.host}/songs/new",
                                 headers={
                                     'Authorization': self.token
                                 },
                                 json={
                                     "song": song.strip()
                                 }
                                 ).json()

        logger.info(response.get('message'))
