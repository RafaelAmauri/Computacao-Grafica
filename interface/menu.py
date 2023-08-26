import PySimpleGUI as sg

from interface.models import configuration, keys, utils
from interface.screens import choose_color

from graphics import translation, scale, rotation, shear, reflection, dda, point_storer
import time

def drawGUI():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layoutScreen


    # Create the Window
    window = sg.Window('My Graphics Library', screens).finalize()
    graph = window[keys.MENU_GRAPH_KEY]


    # Stores points in a a memory-efficient manner providing fast access times as well as fast lookup times.
    # Check the documentation over at pointer_storer.py
    userPoints = point_storer.PointStorer()

    # We have to maintain color cohesion after the transforms, so we use this to store the order that the user
    # has drawn their lines
    userUsedColors = []

    # Check config for default values
    userColor   = config.defaultUserColor

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

            if (clickedX, clickedY) not in userPoints:
                window[keys.X1_COORDINATES_BUTTON_KEY].Update(clickedX)
                window[keys.Y1_COORDINATES_BUTTON_KEY].Update(clickedY)
                
                graph.DrawPoint((clickedX, clickedY), 10, color=userColor)
                
                print(f"Drawed pixel on {clickedX}, {clickedY}")

                # Se não for primeiro ponto, desenhar linha
                if userPoints.numPoints > 0:
                    if algoritmoLinha == "Padrão":
                        graph.DrawLine(point_from=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                point_to=(clickedX, clickedY),
                                color=userColor
                                )

                    elif algoritmoLinha == "DDA":
                        ddaPoints = dda.dda2d(point1=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                            point2=(clickedX, clickedY)
                        )

                        for ddaX, ddaY in ddaPoints:
                            graph.DrawPoint((ddaX, ddaY),
                            4,
                            color=userColor)


                userPoints.add((clickedX, clickedY))
                userUsedColors.append(userColor)

                window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)

                
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
            

            if (selectedX, selectedY) not in userPoints:
                graph.DrawPoint((selectedX, selectedY), 10, color=userColor)

                print(f"Drawed pixel on {selectedX}, {selectedY}")

                # Apenas não desenhamos linhas se tiver só um ponto.
                # Se tiver mais de um ponto, desenhar linha
                if userPoints.numPoints > 0:
                    if algoritmoLinha == "Padrão":
                        graph.DrawLine( point_from=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                        point_to=(selectedX, selectedY),
                                        color=userColor
                                    )
                    
                    elif algoritmoLinha == "DDA":
                        ddaPoints = dda.dda2d(  point1=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                                point2=(selectedX, selectedY)
                        )

                        for pX, pY in ddaPoints:
                            graph.DrawPoint((pX, pY),
                            4,
                            color=userColor)

                userPoints.add((selectedX, selectedY))
                userUsedColors.append(userColor)

                window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)


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

            userPoints.clear()
            userUsedColors  = []

        
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
                userPoints = translation.translation2d(figure=userPoints,
                                                    axis=axisUserChoice,
                                                    x_padding=factorUserChoice,
                                                    y_padding=factorUserChoice
                )

            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Escala":
                userPoints = scale.scale2d(figure=userPoints,
                                        axis=axisUserChoice,
                                        x_scale=factorUserChoice,
                                        y_scale=factorUserChoice
                                        )
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Rotação":
                userPoints = rotation.rotation2d(figure=userPoints,
                                            direction=rotationDirectionUserChoice,
                                            angle=rotationAngleUserChoice
                )
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Cisalinhamento":
                userPoints = shear.shear2d(figure=userPoints,
                                        axis=axisUserChoice,
                                        factor=factorUserChoice
                )
            
            elif values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY] == "Reflexão":
                userPoints = reflection.reflection2d(userPoints,
                                                axis=axisUserChoice
                                                )
            

            # Rewrote previous code to optimize this for loop. Here we remember
            # the values of the previous iteration (in previousX,Y) to avoid having to access 
            # the data in userPoints more than necessary. Before this we were 
            # accessing each point 2x, now it's only once. Hopefully this will translate to
            # one less branch instruction in the assembly code.
            previousX = userPoints.points["x"][0]
            previousY = userPoints.points["y"][0]
            graph.DrawPoint((previousX, previousY), 10, color=userUsedColors[0])

            # idx because we need to access userUsedColors too
            for idx in range(1, userPoints.numPoints):
                currentX = userPoints.points["x"][idx]
                currentY = userPoints.points["y"][idx]
                graph.DrawPoint((currentX, currentY), 10, color=userUsedColors[idx])

                if algoritmoLinha == "Padrão":
                    graph.DrawLine(point_from=(previousX, previousY),
                                    point_to=(currentX, currentY),
                                    color=userUsedColors[idx]
                                )

                elif algoritmoLinha == "DDA":
                    ddaPoints = dda.dda2d(  point1=(previousX, previousY),
                                            point2=(currentX, currentY)
                                            )
                    for ddaX, ddaY in ddaPoints:
                        graph.DrawPoint((ddaX, ddaY),
                                        4,
                                        color=userUsedColors[idx])
                                        
                # Update for the next loop
                previousX = currentX
                previousY = currentY

    window.close()
