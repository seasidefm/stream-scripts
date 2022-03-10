import json

from common.config import get_json_config
from logs.thread_logger import ServiceLogger
from common.mqtt import get_mqtt_client, topics

t_logger = ServiceLogger('heat-level')

config = get_json_config()

print("🔥 Starting heat level file script")


def on_message(_, __, msg):
    payload = json.loads(msg.payload)
    heat_level = payload.get('heat_level') or payload.get('faveCount')

    if not heat_level and heat_level != 0:
        t_logger.error(payload)
        t_logger.error('Could not find `heat_level` or `faveCount` in payload')
        return

    t_logger.info(f"🔥 Received new heat level {heat_level}")

    f = open(config['heat_file'], encoding='utf-8', mode='w')
    if heat_level == 0:
        f.write(f"🔥 HEAT LEVEL RISING")
    else:
        f.write(f"🔥 HEAT LEVEL: {heat_level}")

    f.close()
    t_logger.info("🔥 Heat level set")


def run():
    t_logger.info('🔥 Starting heat level checker')

    client = get_mqtt_client(topics["UPDATE_HEAT"])

    client.connect(config["mqtt_broker"], 5555, 60)
    client.on_message = on_message

    t_logger.info("Client configured and connected")
    t_logger.info("Starting topic subscription loop")
    client.loop_forever()
