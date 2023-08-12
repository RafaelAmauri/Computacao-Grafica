import PySimpleGUI as sg
from interface.models import configuration, keys, utils


def main():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layout_screen


    # Create the Window
    window = sg.Window('Window Title', screens).finalize()
    graph = window[keys.GUI_GRAPH_KEY]


    # Event Loop to process events and get the values of the inputs

    # TODO Check if text in fields is a number
    while True:
        event, values = window.read()
        if event == keys.GUI_DRAW_PIXEL_KEY:
            if values[keys.X1_COORDINATES_BUTTON_KEY] == '' or values[keys.Y1_COORDINATES_BUTTON_KEY] == '':
                utils.create_popup_one_button(window_name="Error", msg_txt="Please give me an X and Y coordinate!", button_txt="Ok!")
                continue

            x1 = int(values[keys.X1_COORDINATES_BUTTON_KEY])
            y1 = int(values[keys.Y1_COORDINATES_BUTTON_KEY])

            point = graph.DrawPoint((x1, y1), 10, color='green')
            print(f"Drawed pixel on {values[keys.X1_COORDINATES_BUTTON_KEY]}, {values[keys.Y1_COORDINATES_BUTTON_KEY]}")

        elif event == keys.GUI_CLOSE_KEY:
            break

    window.close()