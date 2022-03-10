import datetime
import time
from termcolor import colored as color


class ThreadLogger:
    def __init__(self, thread_name: str):
        self.thread_name = thread_name

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

    def log(self, data):
        print(self.thread_timestamp(), data)
