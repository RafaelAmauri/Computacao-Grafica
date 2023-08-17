import PySimpleGUI as sg
from interface.models import keys

class ConfigModel:
    def __init__(self) -> None:
        self.buttonSize   = (40, 1)
        self.inputboxSize = (10, 1)
  
        self.layoutLeft = [
                [sg.Graph(canvas_size=(500, 500), graph_bottom_left=(0,0), graph_top_right=(500, 500), background_color='white', key=keys.MENU_GRAPH_KEY, enable_events=True)]
        ]

        self.layoutRight = [
                [sg.Text(keys.X1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.X1_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.X2_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.X2_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.Y1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.Y1_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.Y2_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.Y2_COORDINATES_BUTTON_KEY)],
                [sg.Button(keys.MENU_DRAW_PIXEL_TEXT, key=keys.MENU_DRAW_PIXEL_KEY), sg.Button(keys.MENU_SELECT_COLOR_TEXT, key=keys.MENU_SELECT_COLOR_KEY)],
                [sg.Button(keys.MENU_CLOSE_TEXT, key=keys.MENU_CLOSE_KEY), sg.Button(keys.MENU_ERASE_TEXT, key=keys.MENU_ERASE_KEY)]
            ]

        self.layoutScreen = [
            [sg.vtop(sg.Column(self.layoutLeft)), sg.VSeparator(), sg.vtop(sg.Column(self.layoutRight))]
        ]
    

    # Getters and Setters
    @property
    def buttonSize(self):
        return self.__buttonSize

    @buttonSize.setter
    def buttonSize(self, size: tuple):
        self.__buttonSize = size

    @property
    def inputboxSize(self):
        return self.__inputboxSize
    @inputboxSize.setter
    def inputboxSize(self, size: tuple):
        self.__inputboxSize = size

    @property
    def layoutScreen(self):
        return self.__layoutScreen
    @layoutScreen.setter
    def layoutScreen(self, layout: list):
        self.__layoutScreen = layout