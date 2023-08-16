import PySimpleGUI as sg
from interface.models import configuration, keys, utils
from interface.screens import choose_color

def drawGUI():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layoutScreen


    # Create the Window
    window = sg.Window('Window Title', screens).finalize()
    graph = window[keys.MENU_GRAPH_KEY]


    # Event Loop to process events and get the values of the inputs

    # TODO Check if text in fields is a number

    # Cor default é vermelho
    color = "#ff0000"

    while True:
        event, values = window.read()
        if event == keys.MENU_GRAPH_KEY:
            graph.DrawPoint(values[keys.MENU_GRAPH_KEY], 10, color=color)
            

        if event == keys.MENU_DRAW_PIXEL_KEY:
            if values[keys.X1_COORDINATES_BUTTON_KEY] == '' or values[keys.Y1_COORDINATES_BUTTON_KEY] == '':
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Please give me X and Y coordinates! Alternatively, you can use the mouse on the Canvas", 
                                            buttonTxt="Ok!")

            else:
                x1 = int(values[keys.X1_COORDINATES_BUTTON_KEY])
                y1 = int(values[keys.Y1_COORDINATES_BUTTON_KEY])

                graph.DrawPoint((x1, y1), 10, color=color)
                print(f"Drawed pixel on {values[keys.X1_COORDINATES_BUTTON_KEY]}, {values[keys.Y1_COORDINATES_BUTTON_KEY]}")

        
        elif event == keys.MENU_SELECT_COLOR_KEY:
            color = choose_color.chooseColor()
            

        elif event == keys.MENU_CLOSE_KEY:
            break

    window.close()