import json


def get_json_config():
    config_json = open('config.json', 'r')
    config = json.loads(config_json.read())
    config_json.close()
    return config
