import PySimpleGUI as sg

from interface.models import configuration, keys, utils
from interface.screens import choose_color, choose_transformation

from graphics import translation, scale, rotation, shear


def drawGUI():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layoutScreen


    # Create the Window
    window = sg.Window('My Graphics Library', screens).finalize()
    graph = window[keys.MENU_GRAPH_KEY]


    # Check config for default values
    userColor = config.defaultUserColor

    points = {
                "x": [],
                "y": []
    }
    usedColors = []


    # Event Loop to process events and get the values of the inputs
    while True:
        event, values = window.read()

        # Clicked on "Exit"
        if event in [keys.MENU_CLOSE_KEY, sg.WIN_CLOSED]:
            break

        # Clicked on graph
        elif event == keys.MENU_GRAPH_KEY:
            clickedX, clickedY = values[keys.MENU_GRAPH_KEY]

            window[keys.X1_COORDINATES_BUTTON_KEY].Update(clickedX)
            window[keys.Y1_COORDINATES_BUTTON_KEY].Update(clickedY)
            
            graph.DrawPoint(values[keys.MENU_GRAPH_KEY], 10, color=userColor)
            
            print(f"Drawed pixel on {clickedX}, {clickedY}")

            # Se não for primeiro ponto, desenhar linha
            if len(points["x"]) > 0:
                graph.DrawLine(point_from=(points["x"][-1], points["y"][-1]),
                               point_to=(clickedX, clickedY),
                               color=userColor
                            )

            usedColors.append(userColor)

            points["x"].append(float(clickedX))
            points["y"].append(float(clickedY))

            window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)
                

        # Clicked on Draw Pixel button
        elif event == keys.MENU_DRAW_PIXEL_KEY:
            try:
                selectedX = float(values[keys.X1_COORDINATES_BUTTON_KEY])
                selectedY = float(values[keys.Y1_COORDINATES_BUTTON_KEY])
            except ValueError:
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Por favor, me dê coordenadas X e Y válidas! Alternativamente, você pode simplesmente clicar no canvas", 
                                            buttonTxt="Ok!")
                continue


            graph.DrawPoint((selectedX, selectedY), 10, color=userColor)

            print(f"Drawed pixel on {selectedX}, {selectedY}")

            # Se não for primeiro ponto, desenhar linha
            if len(points["x"]) > 0:
                graph.DrawLine(point_from=(points["x"][-1], points["y"][-1]),
                                point_to=(selectedX, selectedY),
                                color=userColor
                            )

            usedColors.append(userColor)

            points["x"].append(selectedX)
            points["y"].append(selectedY)

            window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)
        

        # Clicked on select color button
        elif event == keys.MENU_SELECT_COLOR_KEY:
            userColor = choose_color.chooseColor(previousColor=userColor)

        # Clicked on erase button
        elif event == keys.MENU_ERASE_KEY:
            userColor = config.defaultBgColor

            utils.createPopupOneButton(windowName="Apagar",
                                        msgTxt="Borracha selecionada!",
                                        buttonTxt="Ok!"
            )


        # Clicked on erase all button
        elif event == keys.MENU_ERASE_ALL_KEY:
            utils.clearCanvas(graph, config)

            window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=True)

            points["x"] = []
            points["y"] = []
            usedColors  = []

        
        # Clicked on apply transformation button
        elif event == keys.MENU_APPLY_TRANSFORMATION_KEY:
            axisUserChoice = values[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY].lower() if values[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY] in ["X", "Y"] else "both"
            
            try:
                factorUserChoice = float(values[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY])
                rotationAngleUserChoice  = float(values[keys.CHOOSE_TRANSFORMATION_OPTION_ROTATION_ANGLE_KEY])
                rotationDirectionUserChoice = "clockwise" if values[keys.CHOOSE_TRANSFORMATION_OPTION_ROTATION_DIRECTION_KEY] == "Horário" else "anticlockwise"

            except ValueError:
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Por favor, apenas números nos valores \"Fator\" e \"Ângulo\"!", 
                                            buttonTxt="Ok!")
                continue

            utils.clearCanvas(graph, config)

            if values[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Translação":
                points = translation.translation2d(figure=points,
                                                    axis=axisUserChoice,
                                                    x_padding=factorUserChoice,
                                                    y_padding=factorUserChoice
                )

            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Escala":
                points = scale.scale2d(figure=points,
                                        axis=axisUserChoice,
                                        x_scale=factorUserChoice,
                                        y_scale=factorUserChoice
                                        )
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Rotação":
                points = rotation.rotation2d(figure=points,
                                            direction=rotationDirectionUserChoice,
                                            angle=rotationAngleUserChoice
                )
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Cisalinhamento":
                points = shear.shear2d(figure=points,
                                        axis=axisUserChoice,
                                        factor=factorUserChoice
                )
            

            for idx, (tempX, tempY, tempColor) in enumerate(zip(points["x"], points["y"], usedColors)):
                graph.DrawPoint((tempX, tempY), 10, color=tempColor)

                if idx != 0:
                    graph.DrawLine(point_from=(points["x"][idx-1], points["y"][idx-1]),
                                    point_to=(points["x"][idx], points["y"][idx]),
                                    color=tempColor
                                )

    window.close()