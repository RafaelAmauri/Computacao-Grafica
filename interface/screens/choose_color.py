import PySimpleGUI as sg
from interface.models import keys

def chooseColor(previousColor):
    graph = sg.Graph(canvas_size=(50, 50), graph_bottom_left=(0,0), graph_top_right=(50, 50), background_color=previousColor, key=keys.CHOOSE_COLOR_GRAPH_KEY)

    leftSide = [
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=10)],
                    [sg.Text(text=keys.CHOOSE_COLOR_RED_SLIDER_TEXT)],
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=10)],
                    [sg.Text(text=keys.CHOOSE_COLOR_GREEN_SLIDER_TEXT)],
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=10)],
                    [sg.Text(text=keys.CHOOSE_COLOR_BLUE_SLIDER_TEXT)],
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=0)]
    ]

    red   = int(previousColor[1:3], base=16)
    green = int(previousColor[3:5], base=16)
    blue  = int(previousColor[5:7], base=16)

    middle = [
            [sg.Slider(range=(0,255), default_value=red,   orientation='horizontal', key=keys.CHOOSE_COLOR_RED_SLIDER_KEY,   enable_events=True)],
            [sg.Slider(range=(0,255), default_value=green, orientation='horizontal', key=keys.CHOOSE_COLOR_GREEN_SLIDER_KEY, enable_events=True)],
            [sg.Slider(range=(0,255), default_value=blue,  orientation='horizontal', key=keys.CHOOSE_COLOR_BLUE_SLIDER_KEY,  enable_events=True)]
        ]

    rightSide = [
        [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=30)],
        [graph],
        [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=30)]
    ]

    layout = [
        [sg.vtop(sg.Column(leftSide)), sg.VSeparator(), sg.vtop(sg.Column(middle)), sg.VSeparator(), sg.vtop(sg.Column(rightSide))],
        [sg.Button(keys.CHOOSE_COLOR_APPLY_TEXT, key=keys.CHOOSE_COLOR_APPLY_KEY)]
    ]

    screen = sg.Window('Choose color', layout, element_justification='c', finalize=True)

    float2Hex = lambda x: hex(int(x))[2:] if x > 16 else f"{hex(int(x))[2:]}0"

    while True:
        event, values = screen.read()

        if event == sg.WIN_CLOSED or event == keys.CHOOSE_COLOR_APPLY_KEY:
            screen.close()
            break
        
        elif event in [keys.CHOOSE_COLOR_RED_SLIDER_KEY, keys.CHOOSE_COLOR_GREEN_SLIDER_KEY, keys.CHOOSE_COLOR_BLUE_SLIDER_KEY]:
            red_slider   = float2Hex(values[keys.CHOOSE_COLOR_RED_SLIDER_KEY])
            green_slider = float2Hex(values[keys.CHOOSE_COLOR_GREEN_SLIDER_KEY])
            blue_slider  = float2Hex(values[keys.CHOOSE_COLOR_BLUE_SLIDER_KEY])

            color = f"#{red_slider}{green_slider}{blue_slider}"

            graph.draw_rectangle((0,0),(50,50), fill_color=color)


    return color