from threading import Thread

import screen.heat_level
import songs.song_history


def main():
    print('🎵 Starting SeasideFM stream scripts 🎵')

    heat_thread = Thread(target=screen.heat_level.run)
    heat_thread.start()

    song_history = Thread(target=songs.song_history.run)
    song_history.start()


if __name__ == '__main__':
    main()
