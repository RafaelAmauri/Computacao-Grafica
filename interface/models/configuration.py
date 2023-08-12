import PySimpleGUI as sg
from interface.models import keys

class ConfigModel:
    def __init__(self) -> None:
        self.button_size   = (40, 1)
        self.inputbox_size = (10, 1)
  
        self.layout_left = [
                [sg.Graph(canvas_size=(500, 500), graph_bottom_left=(0,0), graph_top_right=(500, 500), background_color='white', key=keys.GUI_GRAPH_KEY)]
        ]

        self.layout_right = [
                [sg.Text(keys.X1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputbox_size, key=keys.X1_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.X2_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputbox_size, key=keys.X2_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.Y1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputbox_size, key=keys.Y1_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.Y2_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputbox_size, key=keys.Y2_COORDINATES_BUTTON_KEY)],
                [sg.Button(keys.GUI_DRAW_PIXEL_TEXT, key=keys.GUI_DRAW_PIXEL_KEY), sg.Button(keys.GUI_SELECT_COLOR_TEXT, key=keys.GUI_SELECT_COLOR_KEY, disabled=True)],
                [sg.Button(keys.GUI_CLOSE_TEXT, key=keys.GUI_CLOSE_KEY)]
            ]

        self.layout_screen = [
            [sg.vtop(sg.Column(self.layout_left)), sg.VSeparator(), sg.vtop(sg.Column(self.layout_right))]
        ]
    

    # Getters and Setters
    @property
    def button_size(self):
        return self.__button_size
    @button_size.setter
    def button_size(self, size: tuple):
        self.__button_size = size

    @property
    def inputbox_size(self):
        return self.__inputbox_size
    @inputbox_size.setter
    def inputbox_size(self, size: tuple):
        self.__inputbox_size = size

    @property
    def layout_screen(self):
        return self.__layout_screen
    @layout_screen.setter
    def layout_screen(self, layout: list):
        self.__layout_screen = layout