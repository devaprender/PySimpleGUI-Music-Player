import os
from pygame import mixer
mixer.init()


def get_files_inside_directory_not_recursive(directory):
    directories = []
    for (root, dirs, files) in os.walk(directory):
        for file in files:
            directories.append(root + os.sep + file)

    return directories


def play_sound(sound_path):
    mixer.music.load(sound_path)
    mixer.music.play()


def stop_sounds():
    mixer.music.stop()


def pause_sounds():
    mixer.music.pause()


def unpause():
    mixer.music.unpause()


def is_sound_playing():
    if mixer.music.get_busy() == True:
        return True
    return False



