import PySimpleGUI as sg

from interface.models import configuration, keys, utils
from interface.screens import choose_color

from graphics import translation, scale, rotation, shear, reflection, dda, point_storer


def drawGUI():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layoutScreen


    # Create the Window
    window = sg.Window('My Graphics Library', screens).finalize()
    graph = window[keys.MENU_GRAPH_KEY]


    # Check config for default values
    userColor   = config.defaultUserColor
    points = point_storer.PointStorer()

    # We have to maintain color cohesion after the transforms, so we use this to store the order that the user
    # has drawn their lines
    usedColors = []


    # Event Loop to process events and get the values of the inputs
    while True:
        event, values  = window.read()
        algoritmoLinha = values[keys.CHOOSE_LINE_ALGORITHM_CHOSEN_OPTION_KEY]

        # Clicked on "Exit"
        if event in [keys.MENU_CLOSE_KEY, sg.WIN_CLOSED]:
            break

        # Clicked on graph
        elif event == keys.MENU_GRAPH_KEY:
            clickedX, clickedY = (int(v) for v in values[keys.MENU_GRAPH_KEY])

            if (clickedX, clickedY) not in points:
                window[keys.X1_COORDINATES_BUTTON_KEY].Update(clickedX)
                window[keys.Y1_COORDINATES_BUTTON_KEY].Update(clickedY)
                
                graph.DrawPoint((clickedX, clickedY), 10, color=userColor)
                
                print(f"Drawed pixel on {clickedX}, {clickedY}")

                # Se não for primeiro ponto, desenhar linha
                if points.numPoints > 0:
                    if algoritmoLinha == "Padrão":
                        graph.DrawLine(point_from=(points.points["x"][-1], points.points["y"][-1]),
                                point_to=(clickedX, clickedY),
                                color=userColor
                                )

                    elif algoritmoLinha == "DDA":
                        ddaPoints = dda.dda2d(point1=(points.points["x"][-1], points.points["y"][-1]),
                                            point2=(clickedX, clickedY)
                        )

                        for ddaX, ddaY in zip(ddaPoints.points["x"], ddaPoints.points["y"]):
                            graph.DrawPoint((ddaX, ddaY),
                            2,
                            color=userColor)


                points.add((clickedX, clickedY))
                usedColors.append(userColor)

                window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)

            else:
                print("JÁ INSERIDO")

        # Clicked on Draw Pixel button
        elif event == keys.MENU_DRAW_PIXEL_KEY:
            try:
                selectedX = int(values[keys.X1_COORDINATES_BUTTON_KEY])
                selectedY = int(values[keys.Y1_COORDINATES_BUTTON_KEY])
            except ValueError:
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Por favor, me dê coordenadas X e Y válidas! Alternativamente, você pode simplesmente clicar no canvas", 
                                            buttonTxt="Ok!")
                continue
            

            if (selectedX, selectedY) not in points:
                graph.DrawPoint((selectedX, selectedY), 10, color=userColor)

                print(f"Drawed pixel on {selectedX}, {selectedY}")

                # Apenas não desenhamos linhas se tiver só um ponto.
                # Se tiver mais de um ponto, desenhar linha
                if len(points["x"]) > 0:
                    if algoritmoLinha == "Padrão":
                        graph.DrawLine( point_from=(points.points["x"][-1], points.points["y"][-1]),
                                        point_to=(selectedX, selectedY),
                                        color=userColor
                                    )
                    
                    elif algoritmoLinha == "DDA":
                        ddaPoints = dda.dda2d(  point1=(points.points["x"][-1], points.points["y"][-1]),
                                                point2=(selectedX, selectedY)
                        )

                        for pX, pY in zip(ddaPoints["x"], ddaPoints["y"]):
                            graph.DrawPoint((pX, pY), 
                            1,
                            color=userColor)

                points.add((selectedX, selectedY))
                usedColors.append(userColor)

                window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)

            else:
                print("JÁ INSERIDO")

        # Clicked on select color button
        elif event == keys.MENU_SELECT_COLOR_KEY:
            userColor = choose_color.chooseColor(previousColor=userColor)

        # Clicked on erase button
        elif event == keys.MENU_ERASE_KEY:
            userColor = config.defaultBgColor
            # window[keys.MENU_ERASER_SIDE_SLIDER_KEY].Update(visible=True)# COMING SOON!

            utils.createPopupOneButton(windowName="Apagar",
                                        msgTxt="Borracha selecionada!",
                                        buttonTxt="Ok!"
            )


        # Clicked on erase all button
        elif event == keys.MENU_ERASE_ALL_KEY:
            utils.clearCanvas(graph, config)

            window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=True)

            points.clear()
            usedColors  = []

        
        # Clicked on apply transformation button
        elif event == keys.MENU_APPLY_TRANSFORMATION_KEY:

            axisUserChoice = values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_AXIS_KEY].lower() if values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_AXIS_KEY] in ["X", "Y"] else "both"
            rotationDirectionUserChoice  =  "clockwise" if values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_ROTATION_DIRECTION_KEY] == "Horário" else "anticlockwise"

            try:
                factorUserChoice             =  float(values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_FACTOR_KEY])
                rotationAngleUserChoice      =  int(values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_ROTATION_ANGLE_KEY])
            except ValueError:
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Por favor, apenas números nos valores \"Fator\" e \"Ângulo\"!", 
                                            buttonTxt="Ok!")
                continue

            utils.clearCanvas(graph, config)

            if values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Translação":
                points = translation.translation2d(figure=points,
                                                    axis=axisUserChoice,
                                                    x_padding=factorUserChoice,
                                                    y_padding=factorUserChoice
                )

            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Escala":
                points = scale.scale2d(figure=points,
                                        axis=axisUserChoice,
                                        x_scale=factorUserChoice,
                                        y_scale=factorUserChoice
                                        )
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Rotação":
                points = rotation.rotation2d(figure=points,
                                            direction=rotationDirectionUserChoice,
                                            angle=rotationAngleUserChoice
                )
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Cisalinhamento":
                points = shear.shear2d(figure=points,
                                        axis=axisUserChoice,
                                        factor=factorUserChoice
                )
            
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Reflexão":
                points = reflection.reflection2d(points,
                                                axis=axisUserChoice
                                                )
            
            for idx, (tempX, tempY, tempColor) in enumerate(zip(points.points["x"], points.points["y"], usedColors)):
                graph.DrawPoint((tempX, tempY), 10, color=tempColor)

                if idx != 0:
                    if algoritmoLinha == "Padrão":
                        graph.DrawLine(point_from=(points.points["x"][idx-1], points.points["y"][idx-1]),
                                        point_to=(points.points["x"][idx], points.points["y"][idx]),
                                        color=tempColor
                                    )

                    elif algoritmoLinha == "DDA":
                        ddaPoints = dda.dda2d(  point1=(points.points["x"][idx-1], points.points["y"][idx-1]),
                                                point2=(points.points["x"][idx], points.points["y"][idx])
                        )

                        for pX, pY in zip(ddaPoints.points["x"], ddaPoints.points["y"]):
                            graph.DrawPoint((pX, pY),
                            2,
                            color=tempColor)

    window.close()
