import logging
import sys
from threading import Thread
from dotenv import load_dotenv

import screen.heat_level
import songs.song_history


def main():
    print('🎵 Starting SeasideFM stream scripts 🎵')

    # Setup ======================================
    load_dotenv()
    logging.basicConfig(
        format="%(message)s %(data)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    # ============================================

    heat_thread = Thread(target=screen.heat_level.run)
    heat_thread.start()

    song_history = Thread(target=songs.song_history.run)
    song_history.start()


if __name__ == '__main__':
    main()
