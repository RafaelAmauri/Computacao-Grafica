import PySimpleGUI as sg

def createPopupOneButton(windowName: str, msgTxt: str, buttonTxt: str):
    sg.Window(windowName,
                    [
                        [sg.Text(msgTxt)],
                        [sg.Button(buttonTxt)]
                    ],
                    element_justification='c').read(close=True)