import PySimpleGUI as sg

def create_popup_one_button(window_name: str, msg_txt: str, button_txt: str):
    sg.Window(window_name,
                    [
                        [sg.Text(msg_txt)],
                        [sg.Button(button_txt)]
                    ],
                    element_justification='c').read(close=True)