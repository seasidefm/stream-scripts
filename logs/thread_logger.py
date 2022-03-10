import datetime
import logging
import sys

from termcolor import colored as color

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s %(data)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)


class ThreadLogger:
    def __init__(self, thread_name: str):
        self.thread_name = thread_name

        self.logger = logging.getLogger(name=self.thread_name)

    @staticmethod
    def get_pretty_time():
        return datetime.datetime.now().strftime('%H:%M:%S')

    @staticmethod
    def cyan(text: str):
        return color(text, 'cyan')

    @staticmethod
    def yellow(text: str):
        return color(text, 'yellow')

    def thread_timestamp(self):
        return f"{self.cyan(self.get_pretty_time())} {self.yellow(f'[{self.thread_name}]')} -"

    def info(self, data):
        self.logger.info(f"{self.thread_timestamp()}", extra={"data": data})
