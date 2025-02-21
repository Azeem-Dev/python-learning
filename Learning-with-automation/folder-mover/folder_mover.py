import os
import sys
import time
import logging
from watchdog.observers import Observer
from mover_handler import MoverHandler


SOURCE_DIR = os.path.join('C:', 'Users', 'HP', 'Downloads')
DEST_DIR_SFX = os.path.join('C:', 'Users', 'HP', 'Downloads', 'SFX')
DEST_DIR_MUSIC = os.path.join('C:', 'Users', 'HP', 'Downloads', 'Music')
DEST_DIR_VIDEO = os.path.join('C:', 'Users', 'HP', 'Downloads', 'Videos')
DEST_DIR_IMAGE = os.path.join('C:', 'Users', 'HP', 'Downloads', 'Images')
DEST_DIR_DOCUMENTS = os.path.join('C:', 'Users', 'HP', 'Downloads', 'Documents')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = MoverHandler(
        SOURCE_DIR, DEST_DIR_SFX, DEST_DIR_MUSIC, DEST_DIR_VIDEO, DEST_DIR_IMAGE, DEST_DIR_DOCUMENTS)
    observer = Observer()
    observer.schedule(event_handler, SOURCE_DIR, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
