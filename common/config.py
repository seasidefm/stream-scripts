import json
from typing import Union

config: Union[dict, None] = None


def get_json_config() -> dict:
    global config

    if config:
        return config
    else:
        config_json = open('config.json', 'r')
        config = json.loads(config_json.read())
        config_json.close()
        return config
