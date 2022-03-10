import os

from twitchAPI.twitch import Twitch


class TwitchStream:
    def __init__(self):
        twitch_app_id = os.environ.get('TWITCH_APP_ID')
        twitch_app_secret = os.environ.get('TWITCH_APP_SECRET')
        self.twitch = Twitch(twitch_app_id, twitch_app_secret)
