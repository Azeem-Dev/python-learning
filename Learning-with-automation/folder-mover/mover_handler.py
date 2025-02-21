from watchdog.events import FileSystemEventHandler
import os
import shutil
import time


def makeUniqueName(name):
    return f'{name}_{time.time()}'


def move(dest, entry, name):

    folder_exists = os.path.exists(dest)
    if not folder_exists:
        os.mkdir(dest)
    else:
        file_exists = os.path.exists(f'{dest}/{name}')
        if file_exists:
            unique_name = makeUniqueName(name)
            os.rename(entry, unique_name)
    shutil.move(entry, dest)


class MoverHandler(FileSystemEventHandler):

    __DOCUMENT_EXTENSIONS = ['.doc', '.docx', '.pdf']
    __IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
    __VIDEO_EXTENSIONS = ['.mp4', '.mkv']
    __AUDIO_EXTENSIONS = ['.mp3', '.wav']

    def __init__(self, source_dir, dest_dir_sfx, dest_dir_music, dest_dir_video, dest_dir_image, dest_dir_documents):
        super().__init__()
        self.source_dir = source_dir
        self.dest_dir_sfx = dest_dir_sfx
        self.dest_dir_music = dest_dir_music
        self.dest_dir_video = dest_dir_video
        self.dest_dir_image = dest_dir_image
        self.dest_dir_documents = dest_dir_documents

    def on_modified(self, event):
        print(event)
        with os.scandir(self.source_dir) as directoryEntries:
            for entry in directoryEntries:
                if entry.name.endswith(tuple(self.__DOCUMENT_EXTENSIONS)):
                    move(self.dest_dir_documents, entry, entry.name)
                elif entry.name.endswith(tuple(self.__VIDEO_EXTENSIONS)):
                    move(self.dest_dir_video, entry, entry.name)
                elif entry.name.endswith(tuple(self.__IMAGE_EXTENSIONS)):
                    move(self.dest_dir_image, entry, entry.name)
                elif entry.name.endswith(tuple(self.__AUDIO_EXTENSIONS)):
                    if entry.name.__contains__('SFX'):
                        move(self.dest_dir_sfx, entry, entry.name)
                    else:
                        move(self.dest_dir_music, entry, entry.name)
