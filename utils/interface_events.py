from utils.interface_utilities import InterfaceUtilities


class InterfaceEvents(InterfaceUtilities):
    def __init__(self, window):
        self.window = window

    def music_has_changed(self, new_name):
        self.window['music_name'].update(new_name)
        self.window['currently_playing'].update(f'Playing: {new_name}')

    def pressed_switch_button(self, new_state):
        switch_button = self.window['switch_state']

        if new_state == 'PAUSE':
            switch_button.update(filename=self.PLAY_MUSIC_IMAGE_PATH)
        else:
            switch_button.update(filename=self.PAUSE_MUSIC_IMAGE_PATH)

    