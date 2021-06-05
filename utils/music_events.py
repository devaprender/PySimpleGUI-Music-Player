from pygame import mixer

from utils.interface_events import InterfaceEvents
from utils.music_utilities import MusicUtilities


class MusicEvents(MusicUtilities):
    def __init__(cls, window):
        cls.interface_events = InterfaceEvents(window)
        super().__init__()

    def _play(cls):
        cls.interface_events.pressed_switch_button("PLAY")
        cls.interface_events.music_has_changed(cls.current_music_name)
        mixer.music.load(cls.current_music)
        mixer.music.play()

    def _stop(cls):
        mixer.music.stop()

    def _pause(cls):
        cls.is_paused = True
        mixer.music.pause()

    def _unpause(cls):
        cls.is_paused = False
        mixer.music.unpause()

    def next(cls):
        cls._stop()

        if cls.current_playing_index + 1 < cls.musics_count:
            cls.current_playing_index += 1
        else:
            print('Reached last music, starting again')
            cls.current_playing_index = 0
        
        cls._play()
        
    def previous(cls):
        cls._stop()

        if cls.current_playing_index - 1 < 0:
            print('Reached first music, playing the last one')
            cls.current_playing_index = cls.musics_count - 1
        else:
            cls.current_playing_index -= 1
        
        cls._play()

    def switch_state(cls):
        if cls.is_playing == True:
            cls.interface_events.pressed_switch_button("PAUSE")
            cls._pause()
        
        elif cls.is_paused == True:
            cls.interface_events.pressed_switch_button("PLAY")
            cls._unpause()

        else:
            cls._play()
        
        
        