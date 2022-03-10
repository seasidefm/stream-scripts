from threading import Thread

import screen.heat_level


def main():
    print('🎵 Starting SeasideFM stream scripts 🎵')

    heat_thread = Thread(target=screen.heat_level.run)
    heat_thread.start()


if __name__ == '__main__':
    main()
