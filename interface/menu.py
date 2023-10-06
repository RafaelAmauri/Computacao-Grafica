import PySimpleGUI as sg

from interface.models import configuration, keys
from interface.screens import choose_color

from graphics import point_storer, circle, clipping_algorithms
from utils import utils

def drawGUI():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layoutScreen


    # Create the Window
    window = sg.Window('My Graphics Library', screens).finalize()
    graph  = window[keys.MENU_GRAPH_KEY]


    # Stores points in a a memory-efficient manner providing fast access times as well as fast lookup times.
    # Check the documentation over at pointer_storer.py
    userPoints = point_storer.PointStorer()

    # We have to maintain color cohesion after the transforms, so we use this to store the order that the user
    # has drawn their lines
    userUsedColors = list()

    # Check config for default values
    functionMapTransformation    = config.functionMapTransformations
    functionMapLineAlgorithm     = config.functionMapLineAlgorithm
    functionMapClippingAlgorithm = config.functionMapClippingAlgorithm
    userColor                    = config.defaultUserColor

    window.move_to_center()
    # Event Loop to process events and get the values of the inputs
    while True:
        event, values  = window.read()

        # Clicked on "Exit"
        if event in [keys.MENU_CLOSE_KEY, sg.WIN_CLOSED]:
            break
        
        # Clicked on graph
        elif event == keys.MENU_GRAPH_KEY:
            lineAlgorithmUserChoice = values[keys.CHOOSE_LINE_ALGORITHM_CHOSEN_OPTION_KEY]
            selectedX, selectedY = (int(v) for v in values[keys.MENU_GRAPH_KEY])

            if (selectedX, selectedY) not in userPoints:
                window[keys.X1_COORDINATES_BUTTON_KEY].Update(selectedX)
                window[keys.Y1_COORDINATES_BUTTON_KEY].Update(selectedY)
                
                graph.DrawPoint((selectedX, selectedY), 10, color=userColor)
                
                print(f"Drew pixel on {selectedX}, {selectedY}")

                # Se não for primeiro ponto, desenhar linha
                if userPoints.numPoints > 0:
                    if lineAlgorithmUserChoice == "Padrão":
                        graph.DrawLine(point_from=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                point_to=(selectedX, selectedY),
                                color=userColor
                                )


                    else:
                        functionLineAlgorithm = functionMapLineAlgorithm[lineAlgorithmUserChoice]
                        functionLineAlgorithm(  graph=graph,
                                                startPoint=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                                endPoint=(selectedX, selectedY),
                                                color=userColor
                                            )


                userPoints.add((selectedX, selectedY))
                userUsedColors.append(userColor)

                window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)



                
        # Clicked on Draw Pixel button
        elif event == keys.MENU_DRAW_PIXEL_KEY:
            lineAlgorithmUserChoice = values[keys.CHOOSE_LINE_ALGORITHM_CHOSEN_OPTION_KEY]
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
                print(f"Drew pixel on {selectedX}, {selectedY}")

                # Algorithms have built-in functions that skip the operations if point1 and point2 are the same.
                if userPoints.numPoints > 0:
                    if lineAlgorithmUserChoice == "Padrão":
                        graph.DrawLine( point_from=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                        point_to=(selectedX, selectedY),
                                        color=userColor
                                        )
                    else:
                        functionLineAlgorithm = functionMapLineAlgorithm[lineAlgorithmUserChoice]
                        functionLineAlgorithm(  graph=graph,
                                                startPoint=(userPoints.points["x"][-1], userPoints.points["y"][-1]),
                                                endPoint=(selectedX, selectedY),
                                                color=userColor
                                                )

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
            


        # Clicked on Draw Circle button
        elif event == keys.MENU_DRAW_CIRCLE_KEY:
            selectedX = int(values[keys.X1_COORDINATES_BUTTON_KEY])
            selectedY = int(values[keys.Y1_COORDINATES_BUTTON_KEY])
            circleRadius = int(values[keys.MENU_CIRCLE_RADIUS_KEY])
            circleResolution = int(values[keys.MENU_CIRCLE_NPOINTS_KEY])

            circlePoints = circle.circle2d( origin=(selectedX, selectedY), 
                                            radius=circleRadius, 
                                            resolution=circleResolution
                                            )

            for x, y in circlePoints:
                graph.DrawPoint((x,y), 10, color=userColor)


        # Clicked on apply clipping button
        elif event == keys.MENU_APPLY_CLIPPING_KEY:
            # Parse values for X and Y Limits
            try:
                xmin = int(values[keys.MIN_X_VALUE_CLIPPING_KEY])
                xmax = int(values[keys.MAX_X_VALUE_CLIPPING_KEY])
                ymin = int(values[keys.MIN_Y_VALUE_CLIPPING_KEY])
                ymax = int(values[keys.MAX_Y_VALUE_CLIPPING_KEY])
            except ValueError:
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Por favor, me dê coordenadas válidas para o recorte!", 
                                            buttonTxt="Ok!")
                continue
            
            xLimits = (xmin, xmax)
            yLimits = (ymin, ymax)

            clippingAlgorithmUserChoice = values[keys.CHOOSE_CLIPPING_ALGORITHM_CHOSEN_OPTION_KEY]
            functionClippingUserChoice  = functionMapClippingAlgorithm[clippingAlgorithmUserChoice]
            # Clear canvas so we can only show the lines inside the clipping bounds
            utils.clearCanvas(graph, config)
            # Draw red rectangle to draw where the bounds are
            graph.DrawRectangle((xmin, ymin), (xmax, ymax), line_color="red")


            previousX = userPoints.points["x"][0]
            previousY = userPoints.points["y"][0]
            # idx because we need to access userUsedColors too
            for idx in range(1, userPoints.numPoints):
                currentX = userPoints.points["x"][idx]
                currentY = userPoints.points["y"][idx]

                clippingResults = functionClippingUserChoice((previousX, previousY), 
                                                             (currentX, currentY), 
                                                             xLimits,
                                                             yLimits)

                isAccepted, ((clippedX1, clippedY1), (clippedX2, clippedY2)) = clippingResults

                if isAccepted:
                    lineAlgorithmUserChoice = values[keys.CHOOSE_LINE_ALGORITHM_CHOSEN_OPTION_KEY]
                    
                    if lineAlgorithmUserChoice == "Padrão":
                        graph.DrawLine(point_from=(clippedX1, clippedY1),
                                       point_to=(clippedX2, clippedY2),
                                       color=userUsedColors[idx]
                                    )

                    else:
                        functionLineAlgorithm = functionMapLineAlgorithm[lineAlgorithmUserChoice]
                        functionLineAlgorithm(graph=graph,
                                            startPoint=(clippedX1, clippedY1),
                                            endPoint=(clippedX2, clippedY2),
                                            color=userUsedColors[idx]
                                            )
                
                # Update for the next loop
                previousX = currentX
                previousY = currentY

            

        # Clicked on apply transformation button
        elif event == keys.MENU_APPLY_TRANSFORMATION_KEY:
            lineAlgorithmUserChoice      = values[keys.CHOOSE_LINE_ALGORITHM_CHOSEN_OPTION_KEY]
            transformationUserChoice     = values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_TRANSFORMATION_KEY]
            axisUserChoice               = values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_AXIS_KEY].lower() if values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_AXIS_KEY] in ["X", "Y"] else "both"
            rotationDirectionUserChoice  = "clockwise" if values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_ROTATION_DIRECTION_KEY] == "Horário" else "anticlockwise"
            
            try:
                factorUserChoice             =  float(values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_FACTOR_KEY])
                rotationAngleUserChoice      =  int(values[keys.CHOOSE_TRANSFORMATION_OPTION_CHOSEN_ROTATION_ANGLE_KEY])
            except ValueError:
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Por favor, apenas números nos valores \"Fator\" e \"Ângulo\"!", 
                                            buttonTxt="Ok!")
                continue

            utils.clearCanvas(graph, config)

            # Maps the transformation the user chose on the GUI to a function. The binds can
            # be checked over at configuration.py.
            functionTransformationUserChoice = functionMapTransformation[transformationUserChoice]

            # Calculates the new points after performing the transformation
            userPoints = functionTransformationUserChoice(  figure=userPoints,
                                                            axis=axisUserChoice,
                                                            factor=factorUserChoice,
                                                            direction=rotationDirectionUserChoice,
                                                            angle=rotationAngleUserChoice
                                                            )
            

            previousX = userPoints.points["x"][0]
            previousY = userPoints.points["y"][0]
            graph.DrawPoint((previousX, previousY), 10, color=userUsedColors[0])
            # idx because we need to access userUsedColors too
            for idx in range(1, userPoints.numPoints):
                currentX = userPoints.points["x"][idx]
                currentY = userPoints.points["y"][idx]
                graph.DrawPoint((currentX, currentY), 10, color=userUsedColors[idx])

                if lineAlgorithmUserChoice == "Padrão":
                    graph.DrawLine(point_from=(previousX, previousY),
                                    point_to=(currentX, currentY),
                                    color=userUsedColors[idx]
                                )

                else:
                    functionLineAlgorithm = functionMapLineAlgorithm[lineAlgorithmUserChoice]
                    functionLineAlgorithm(  graph=graph,
                                            startPoint=(previousX, previousY),
                                            endPoint=(currentX, currentY),
                                            color=userUsedColors[idx]
                                            )

                # Update for the next loop
                previousX = currentX
                previousY = currentY

        elif event == keys.MENU_APPLY_FILL_KEY:
            from graphics.fill_algorithms import boundaryFill, _boundaryFill

            x = 0
            y = 0
            boundaryFill(graph, (x,y), userPoints, userUsedColors, "#000000")


    window.close()