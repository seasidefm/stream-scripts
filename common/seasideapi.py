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
        logger.info("Getting current song")
        response = requests.get("https://api.seaside.fm/songs/current", headers={
            'Authorization': self.token
        }).json()

        song_dict = response.get('data')

        return f"{song_dict.get('artist')} - {song_dict.get('song')}"

    def add_song_to_history(self, song: str):
        logger.info(f"Adding new song: {song}")
        response = requests.post("https://api.seaside.fm/songs/new",
                                 headers={
                                     'Authorization': self.token
                                 },
                                 json={
                                     "song": song.strip()
                                 }
                                 ).json()

        logger.info(response.get('message'))
