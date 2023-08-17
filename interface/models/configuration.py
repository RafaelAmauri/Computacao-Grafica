import PySimpleGUI as sg
from interface.models import keys

class ConfigModel:
    def __init__(self) -> None:
        self.buttonSize     = (40, 1)
        self.inputboxSize   = (10, 1)
        self.canvasSize     = (500,500)

        self.defaultBgColor   = "#ffffff"
        self.defaultUserColor = "#000000"

        self.defaultUserTransformations = {
                                    keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY: "Translação",
                                    keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY: "both",
                                    keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY: 2
        }
  
        self.layoutLeft = [
                [sg.Graph(canvas_size=self.canvasSize, graph_bottom_left=(0,0), graph_top_right=self.canvasSize, background_color=self.defaultBgColor, key=keys.MENU_GRAPH_KEY, enable_events=True)]
        ]

        self.layoutRight1 = [
                [sg.Text(keys.X1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.X1_COORDINATES_BUTTON_KEY), sg.Text(keys.Y1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.Y1_COORDINATES_BUTTON_KEY)],
                [sg.Text(keys.X2_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.X2_COORDINATES_BUTTON_KEY), sg.Text(keys.Y2_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.Y2_COORDINATES_BUTTON_KEY)],
            ]

        self.layoutRight2 = [
                [sg.Button(keys.MENU_DRAW_PIXEL_TEXT, key=keys.MENU_DRAW_PIXEL_KEY), sg.Button(keys.MENU_SELECT_COLOR_TEXT, key=keys.MENU_SELECT_COLOR_KEY)],
                [sg.Button(keys.MENU_CLOSE_TEXT, key=keys.MENU_CLOSE_KEY), sg.Button(keys.MENU_ERASE_TEXT, key=keys.MENU_ERASE_KEY), sg.Button(keys.MENU_ERASE_ALL_TEXT, key=keys.MENU_ERASE_ALL_KEY)],
                [sg.Button(keys.MENU_SELECT_TRANSFORMATION_TEXT, key=keys.MENU_SELECT_TRANSFORMATION_KEY), sg.Button(keys.MENU_APPLY_TRANSFORMATION_TEXT, key=keys.MENU_APPLY_TRANSFORMATION_KEY, disabled=True)]
        ]

        self.layoutScreen = [
            [sg.vtop(sg.Column(self.layoutLeft)), sg.VSeparator(), sg.vtop(sg.Column(self.layoutRight1)), sg.VSeparator(), sg.vtop(sg.Column(self.layoutRight2))]
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
    def canvasSize(self):
        return self.__canvasSize
    
    @canvasSize.setter
    def canvasSize(self, size: tuple):
        self.__canvasSize = size

    @property
    def defaultBgColor(self):
        return self.__defaultBgColor

    @defaultBgColor.setter
    def defaultBgColor(self, color: str):
        self.__defaultBgColor = color

    @property
    def defaultUserColor(self):
        return self.__defaultUserColor

    @defaultUserColor.setter
    def defaultUserColor(self, color: str):
        self.__defaultUserColor = color

    @property
    def defaultUserTransformations(self):
        return self.__defaultUserTransformations
    
    @defaultUserTransformations.setter
    def defaultUserTransformations(self, transformations: dict):
        self.__defaultUserTransformations = transformations

    @property
    def layoutScreen(self):
        return self.__layoutScreen
    @layoutScreen.setter
    def layoutScreen(self, layout: list):
        self.__layoutScreen = layout