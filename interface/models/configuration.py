import PySimpleGUI as sg
from interface.models import keys

class ConfigModel:
    def __init__(self) -> None:
        self.textBoxSize    = (12, 1)
        self.inputboxSize   = (12, 1)
        self.buttonSize     = (20, 1)
        self.canvasSize     = (600,600)

        self.defaultBgColor   = "#ffffff"
        self.defaultUserColor = "#000000"
        
        self.transformationOptions = [
                    ["Operação", ["Translação", "Escala", "Rotação", "Cisalinhamento", "Reflexão"]],
                    ["Eixo", ["X", "Y", "Ambos"]],
                    ["Fator da Transformação"],
                    ["Angulo de Rotação"],
                    ["Direção da Rotação", ["Horário", "Anti-Horário"]]
        ]

        self.algorithmOptions = [
            [keys.CHOOSE_LINE_ALGORITHM_DROPDOWN_TEXT, [keys.CHOOSE_LINE_ALGORITHM_CHOICE_1, keys.CHOOSE_LINE_ALGORITHM_CHOICE_2]]
        ]
  
        self.layoutLeft = [
                [sg.Graph(canvas_size=self.canvasSize, graph_bottom_left=(0,0), graph_top_right=self.canvasSize, background_color=self.defaultBgColor, key=keys.MENU_GRAPH_KEY, enable_events=True)]
        ]

        self.layoutMiddle1 = [
                [sg.Text(keys.X1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.X1_COORDINATES_BUTTON_KEY)],
                [sg.HSeparator()],
                [sg.Button(keys.MENU_DRAW_PIXEL_TEXT, key=keys.MENU_DRAW_PIXEL_KEY, size=self.buttonSize)],
                [sg.Button(keys.MENU_ERASE_TEXT, key=keys.MENU_ERASE_KEY, size=self.buttonSize)]
                ]

        self.layoutMiddle2 = [
            [sg.Text(keys.Y1_COORDINATES_BUTTON_TEXT), sg.InputText(size=self.inputboxSize, key=keys.Y1_COORDINATES_BUTTON_KEY)],
            [sg.HSeparator()],
            [sg.Button(keys.MENU_SELECT_COLOR_TEXT, key=keys.MENU_SELECT_COLOR_KEY, size=self.buttonSize)],
            [sg.Button(keys.MENU_ERASE_ALL_TEXT, key=keys.MENU_ERASE_ALL_KEY, size=self.buttonSize)],
            [sg.Button(keys.MENU_APPLY_TRANSFORMATION_TEXT, key=keys.MENU_APPLY_TRANSFORMATION_KEY, size=self.buttonSize, disabled=True)]
        ]

        self.layoutRight1 = [
                [sg.Text(self.transformationOptions[0][0], pad=(self.textBoxSize,self.textBoxSize))],
                [sg.Text(self.transformationOptions[1][0], pad=(self.textBoxSize,self.textBoxSize))],
                [sg.Text(self.transformationOptions[2][0], pad=(self.textBoxSize,25))],
                [sg.Text(self.transformationOptions[3][0], pad=(self.textBoxSize,1))],
                [sg.Text(self.transformationOptions[4][0], pad=(self.textBoxSize,self.textBoxSize))],
                [sg.Text(self.algorithmOptions[0][0],      pad=(self.textBoxSize,self.textBoxSize))]
        ]

        self.layoutRight2 = [
            [sg.OptionMenu(
                values=(self.transformationOptions[0][1]), 
                size=self.inputboxSize, 
                default_value=keys.CHOOSE_TRANSFORMATION_OPTION_DEFAULT_TRANSFORMATION, 
                key=keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY
                )],
            
            [sg.OptionMenu(
                values=(self.transformationOptions[1][1]), 
                size=self.inputboxSize, 
                default_value=keys.CHOOSE_TRANSFORMATION_OPTION_DEFAULT_AXIS, 
                key=keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_AXIS_KEY
                )],
            
            [sg.Slider(
                range=(-10,10), 
                default_value=keys.CHOOSE_TRANSFORMATION_OPTION_DEFAULT_FACTOR, 
                resolution=0.5,
                orientation="horizontal", 
                key=keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_FACTOR_KEY
                )],
            
            [sg.Slider(
                range=(0,359), 
                default_value=keys.CHOOSE_TRANSFORMATION_OPTION_DEFAULT_ROTATION_ANGLE, 
                resolution=1, 
                orientation="horizontal", 
                key=keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_ROTATION_ANGLE_KEY
                )],
            
            [sg.OptionMenu(
                values=(self.transformationOptions[4][1]), 
                size=self.inputboxSize, 
                default_value=keys.CHOOSE_TRANSFORMATION_OPTION_DEFAULT_ROTATION_DIRECTION, 
                key=keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_ROTATION_DIRECTION_KEY
                )],
            
            [sg.OptionMenu(
                values=self.algorithmOptions[0][1], 
                size=self.inputboxSize, 
                default_value=keys.CHOOSE_LINE_ALGORITHM_DEFAULT_OPTION, 
                key=keys.CHOOSE_LINE_ALGORITHM_CHOSEN_OPTION_KEY
                )]
        ]

        self.layoutBottom = [
            [sg.Button(keys.MENU_CLOSE_TEXT, key=keys.MENU_CLOSE_KEY),]
        ]

        # 3 Columns
        self.layoutScreen = [
            [
                sg.vtop(sg.Column(self.layoutLeft)), sg.VSeparator(), 
                sg.vtop(sg.Column(self.layoutMiddle1)), sg.vtop(sg.Column(self.layoutMiddle2)), sg.VSeparator(),
                sg.vtop(sg.Column(self.layoutRight1)), sg.vtop(sg.Column(self.layoutRight2)), sg.vbottom(sg.Column(self.layoutBottom))]
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