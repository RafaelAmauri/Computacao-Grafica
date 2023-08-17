import PySimpleGUI as sg
from interface.models import configuration, keys

config = configuration.ConfigModel()

def chooseTransformation(previousChoices):
    options = [
                    ["Transformação", ["Translação", "Escala", "Rotação"]],
                    ["Eixo", ["X", "Y", "Ambos"]],
                    ["Fator da Transformação"]
    ]

    if previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] != "both":
        previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] = previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY].upper()
    else:
        previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] = "Ambos"
    
    layout = [
        [sg.Text(options[0][0], pad=((3,0),0)), sg.OptionMenu(values = (options[0][1]), size=(20,1), default_value=previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY], key=keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY)],
        [sg.Text(options[1][0], pad=((3,0),0)), sg.OptionMenu(values = (options[1][1]), size=(20,1), default_value=previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY], key=keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY)],
        [sg.Text(options[2][0], pad=((3,0),0)), sg.InputText(size=config.inputboxSize, default_text=previousChoices[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY], key=keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY)],
        [sg.Button(keys.CHOOSE_TRANSFORMATION_APPLY_TEXT, key=keys.CHOOSE_TRANSFORMATION_APPLY_KEY)]
    ]

    screen = sg.Window('Choose Transformation', layout, element_justification='c', finalize=True)

    while True:
        event, values = screen.read()

        if event == sg.WIN_CLOSED or event == keys.CHOOSE_TRANSFORMATION_APPLY_KEY:
            screen.close()
            break
    
    values[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY] = float(values[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY])
    if values[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] == "Ambos":
        values[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] = "both"
    else:
        values[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] = values[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY].lower()

    return values