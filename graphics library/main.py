import scale, translation, utils

# Triangulo 3-4-5
triangulo1 = {
                "x": [6, 6, 18, 6],
                "y": [6, 15, 6, 6]
}

quadrado1 = {
                "x": [1, 1, 15, 15, 1],
                "y": [1, 15, 15, 1, 1]
}

utils.show_figure(quadrado1)

#triangulo1_transformed = translation.translation2d(triangulo1.copy(), axis="both", y_padding=2, x_padding=2)
quadrado1_scaled = scale.scale2d(quadrado1.copy(), axis="both", x_scale=1, y_scale=0.5)

utils.show_figure(quadrado1, quadrado1_scaled)