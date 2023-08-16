import PySimpleGUI as sg
from interface.models import keys

def chooseColor():
    graph = sg.Graph(canvas_size=(50, 50), graph_bottom_left=(0,0), graph_top_right=(50, 50), background_color='white', key=keys.CHOOSE_COLOR_GRAPH_KEY)

    leftSide = [
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=10)],
                    [sg.Text(text=keys.CHOOSE_COLOR_RED_SLIDER_TEXT)],
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=10)],
                    [sg.Text(text=keys.CHOOSE_COLOR_GREEN_SLIDER_TEXT)],
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=10)],
                    [sg.Text(text=keys.CHOOSE_COLOR_BLUE_SLIDER_TEXT)],
                    [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=0)]
    ]

    middle = [
            [sg.Slider(range=(0,255), default_value=255, orientation='horizontal', key=keys.CHOOSE_COLOR_RED_SLIDER_KEY)],
            [sg.Slider(range=(0,255), default_value=255, orientation='horizontal', key=keys.CHOOSE_COLOR_GREEN_SLIDER_KEY)],
            [sg.Slider(range=(0,255), default_value=255, orientation='horizontal', key=keys.CHOOSE_COLOR_BLUE_SLIDER_KEY)]
        ]

    rightSide = [
        [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=30)],
        [graph],
        [sg.HSeparator(color=sg.DEFAULT_BACKGROUND_COLOR, pad=30)]
    ]

    layout = [
        [sg.vtop(sg.Column(leftSide)), sg.VSeparator(), sg.vtop(sg.Column(middle)), sg.VSeparator(), sg.vtop(sg.Column(rightSide))],
        [sg.Button(keys.CHOOSE_COLOR_PREVIEW_TEXT, key=keys.CHOOSE_COLOR_PREVIEW_KEY), sg.Button(keys.CHOOSE_COLOR_APPLY_TEXT, key=keys.CHOOSE_COLOR_APPLY_KEY)]
    ]

    screen = sg.Window('Choose color', layout, element_justification='c', finalize=True)

    while True:
        event, values = screen.read()

        if event == sg.WIN_CLOSED or event == keys.CHOOSE_COLOR_APPLY_KEY:
            screen.close()
            break
        
        elif event == keys.CHOOSE_COLOR_PREVIEW_KEY:
            float2Hex = lambda x: hex(int(x))[2:] if x > 16 else f"{hex(int(x))[2:]}0"

            red_slider   = float2Hex(values[keys.CHOOSE_COLOR_RED_SLIDER_KEY])
            green_slider = float2Hex(values[keys.CHOOSE_COLOR_GREEN_SLIDER_KEY])
            blue_slider  = float2Hex(values[keys.CHOOSE_COLOR_BLUE_SLIDER_KEY])

            color = f"#{red_slider}{green_slider}{blue_slider}"

            graph.draw_rectangle((0,0),(50,50), fill_color=color)


    '''
    Feio ter que fazer a função lambda de novo, mas pode ser que o usuário só escolha uma cor sem fazer
    a preview, e a gente precisa fazer essa conta pelo menos uma vez. A alternativa é fazer 
    isso já dentro do loop, mas isso piora a performance porque senão essa conta vai ser feita 
    a cada frame draw, ou seja, a cada vez que o user mexer no slider, etc.
    Da forma que está agora o custo é bem baixo: O(N+1), com N = numero de vezes que o user 
    renderiza uma cor.
    '''
    float2Hex = lambda x: hex(int(x))[2:] if x > 16 else f"{hex(int(x))[2:]}0"

    red_slider   = float2Hex(values[keys.CHOOSE_COLOR_RED_SLIDER_KEY])
    green_slider = float2Hex(values[keys.CHOOSE_COLOR_GREEN_SLIDER_KEY])
    blue_slider  = float2Hex(values[keys.CHOOSE_COLOR_BLUE_SLIDER_KEY])

    color = f"#{red_slider}{green_slider}{blue_slider}"

    return color