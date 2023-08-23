import PySimpleGUI as sg

def createPopupOneButton(windowName: str, msgTxt: str, buttonTxt: str):
    sg.Window(windowName,
                    [
                        [sg.Text(msgTxt)],
                        [sg.Button(buttonTxt)]
                    ],
                    element_justification='c').read(close=True)

def clearCanvas(graph, config):
    graph.DrawRectangle(top_left=(0,0),
                                bottom_right=config.canvasSize,
                                fill_color=config.defaultBgColor
                )
    
    return graph