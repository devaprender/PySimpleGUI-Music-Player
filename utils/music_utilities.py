import os

import PySimpleGUI as sg
from pygame import mixer

from utils.cache import Cache

class MusicUtilities:
    def __init__(cls):
        mixer.init()
        cls.musics = []
        cls.musics_count = 0
        cls.current_playing_index = 0
        cls.is_paused = False
        cls.musics_dir_key = "md"
        cls._load_music_directories()

    def _get_musics_inside_directory(cls, directory):
        directories = []

        for (root, _, files) in os.walk(directory):
            for file in files:
                directories.append(root + os.sep + file)

        return directories
    
    def _load_music_directories(cls):
        cache = Cache()
        directory = cache.read(cls.musics_dir_key)
        
        if directory == None:
            directory = sg.popup_get_folder('Select Music Directory')
            cache.save(cls.musics_dir_key, directory)

        cls.musics = cls._get_musics_inside_directory(directory)
        cls.musics_count = len(cls.musics)

    @property
    def current_music(cls):
        return cls.musics[cls.current_playing_index]

    @property
    def current_music_name(cls):
        return os.path.basename(cls.current_music)

    @property
    def is_playing(cls):
        if mixer.music.get_busy() == True:
            return True
        return False