import os

import PySimpleGUI as sg


class InterfaceUtilities:
    GO_BACK_IMAGE_PATH = os.path.join('images', 'back.png')
    GO_FORWARD_IMAGE_PATH = os.path.join('images', 'next.png')
    PLAY_MUSIC_IMAGE_PATH = os.path.join('images', 'play.png')
    PAUSE_MUSIC_IMAGE_PATH = os.path.join('images', 'pause.png')
    album_cover_image_path = os.path.join('images', 'pylot.png')
        
    def _create_main_layout(cls):
        music_title = [
            [sg.Text(text='Press play...', 
                     justification='center', 
                     background_color='black',
                     text_color='white', 
                     size=(200, 0), 
                     font='Tahoma', 
                     key='music_name')]
        ]

        author_info = [
            [sg.Text(text='PySimpleGUI Player - By youtube.com/devaprender',
                     background_color='black', 
                     text_color='white',  
                     font=('Tahoma', 7))]
        ]

        currently_playing = [
            [sg.Text(background_color='black', 
                     size=(200, 0), 
                     text_color='white',
                     font=('Tahoma', 10), 
                     key='currently_playing')]
        ]

        main_layout = [
            [sg.Canvas(background_color='black', size=(480, 20))],
            [sg.Column(layout=author_info, 
                       justification='c',
                       element_justification='c', 
                       background_color='black')],

            [
                sg.Canvas(background_color='black', size=(40, 350)),
                sg.Image(filename=cls.album_cover_image_path, 
                         size=(350, 350),
                         key="cover"),
                sg.Canvas(background_color='black', size=(40, 350))
            ],

            [sg.Canvas(background_color='black', size=(480, 10))],
            [sg.Column(layout=music_title, 
                       background_color='black',
                       justification='c', 
                       element_justification='c')],
            [sg.Text(text= '_' * 80, background_color='black', text_color='white')],

            [
                sg.Canvas(background_color='black', size=(99, 200), pad=(10, 0)),

                sg.Image(pad=(20, 0), 
                         filename=cls.GO_BACK_IMAGE_PATH, 
                         enable_events=True,
                         size=(35, 44), 
                         key='previous', 
                         background_color='black'),

                sg.Image(filename=cls.PLAY_MUSIC_IMAGE_PATH,
                         size=(35, 44), 
                         pad=(20, 0), 
                         enable_events=True, 
                         key='switch_state', 
                         background_color='black'),

                sg.Image(filename=cls.GO_FORWARD_IMAGE_PATH, 
                         enable_events=True,
                         size=(35, 44), 
                         pad=(20, 0), 
                         key='next', 
                         background_color='black'),
            ],

            [sg.Column(layout=currently_playing, 
                       justification='c',
                       element_justification='c', 
                       background_color='black')]
        ]

        return main_layout

    def create_window(cls):
        main_layout = cls._create_main_layout()
        window = sg.Window('Spotify', 
                            layout=main_layout, 
                            size=(480, 730), 
                            background_color='black', 
                            finalize=True, 
                            grab_anywhere=True, 
                            resizable=False)
        
        return window