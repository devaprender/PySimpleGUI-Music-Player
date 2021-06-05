import PySimpleGUI as sg

from utils.interface_utilities import InterfaceUtilities
from utils.music_events import MusicEvents


class Core(MusicEvents):
    def __init__(cls):
        sg.theme('Reddit')
        interface_utilities = InterfaceUtilities()
        cls.window = interface_utilities.create_window() 
        super().__init__(cls.window)
        cls._start()

    def _start(cls):
        while True:
            event, _ = cls.window.read()

            if event == sg.WIN_CLOSED:
                break

            elif event == 'switch_state':
                cls.switch_state()
                    
            elif event == 'next':
                cls.next()

            elif event == 'previous':
                cls.previous()

Core()