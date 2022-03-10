from twitchAPI.twitch import Twitch

from common.config import get_json_config
from logs.thread_logger import ServiceLogger

logger = ServiceLogger('twitch')


class TwitchStream:
    def __init__(self):
        config = get_json_config()
        logger.info("Initializing Twitch service")
        self.twitch = Twitch(config.get('twitch_app_id'), config.get('twitch_app_secret'))

    def is_live(self) -> bool:
        stream_data = self.twitch.get_streams(user_login=["seasidefm"])
        return bool(len(stream_data.get('data')))
