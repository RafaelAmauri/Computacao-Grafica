import PySimpleGUI as sg

from interface.models import configuration, keys, utils
from interface.screens import choose_color, choose_transformation

from graphics import translation, scale, rotation, shear


def drawGUI():
    sg.theme('DarkAmber') # Add a touch of color

    config  = configuration.ConfigModel()
    screens = config.layoutScreen


    # Create the Window
    window = sg.Window('Window Title', screens).finalize()
    graph = window[keys.MENU_GRAPH_KEY]


    # Event Loop to process events and get the values of the inputs

    # TODO Check if text in fields is a number
    # TODO Implementar todas as transformações geométricas

    # Check config for default values
    userColor           = config.defaultUserColor
    userTransformations = config.defaultUserTransformations

    points = {
                "x": [],
                "y": []
    }


    while True:
        event, values = window.read()

        # Clicked on "Exit"
        if event == keys.MENU_CLOSE_KEY:
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
            
            points["x"].append(clickedX)
            points["y"].append(clickedY)
                

        # Clicked on Draw Pixel button
        elif event == keys.MENU_DRAW_PIXEL_KEY:
            if values[keys.X1_COORDINATES_BUTTON_KEY] == '' or values[keys.Y1_COORDINATES_BUTTON_KEY] == '':
                utils.createPopupOneButton(windowName="Error", 
                                            msgTxt="Please give me X and Y coordinates! Alternatively, you can use the mouse on the Canvas", 
                                            buttonTxt="Ok!")

            else:

                graph.DrawPoint((int(values[keys.X1_COORDINATES_BUTTON_KEY]), int(values[keys.Y1_COORDINATES_BUTTON_KEY])), 10, color=userColor)

                print(f"Drawed pixel on {values[keys.X1_COORDINATES_BUTTON_KEY]}, {values[keys.Y1_COORDINATES_BUTTON_KEY]}")

                # Se não for primeiro ponto, desenhar linha
                if len(points["x"]) > 0:
                    graph.DrawLine(point_from=(points["X"][-1], points["Y"][-1]),
                                    point_to=(clickedX, clickedY),
                                    color=userColor
                                )
                
                points["x"].append(values[keys.X1_COORDINATES_BUTTON_KEY])
                points["y"].append(values[keys.Y1_COORDINATES_BUTTON_KEY])
        

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

            points["x"] = []
            points["y"] = []


        # Clicked on select transformation button
        elif event == keys.MENU_SELECT_TRANSFORMATION_KEY:
            userTransformations = choose_transformation.chooseTransformation(previousChoices=userTransformations)
            window[keys.MENU_APPLY_TRANSFORMATION_KEY].Update(disabled=False)

        
        # Clicked on apply transformation button
        elif event == keys.MENU_APPLY_TRANSFORMATION_KEY:
            utils.clearCanvas(graph, config)
            
            if userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Translação":
                points = translation.translation2d(figure=points,
                                                    axis=userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY],
                                                    x_padding=userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY],
                                                    y_padding=userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY]
                )

            elif userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Escala":
                points = scale.scale2d(figure=points,
                                        axis=userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_AXIS_KEY],
                                        x_scale=userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY],
                                        y_scale=userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_FACTOR_KEY]
                                        )
            elif userTransformations[keys.CHOOSE_TRANSFORMATION_OPTION_TRANSFORMATION_KEY] == "Rotação":
                pass
            

            for idx, (tempX, tempY) in enumerate(zip(points["x"], points["y"])):
                graph.DrawPoint((tempX, tempY), 10, color=userColor)

                if idx != 0:
                    graph.DrawLine(point_from=(points["x"][idx-1], points["y"][idx-1]),
                                    point_to=(points["x"][idx], points["y"][idx]),
                                    color=userColor
                                )

    window.close()