import matplotlib.pyplot as plt

def show_figure(original_figure: dict, new_figure:dict=None):
    plt.ylim(bottom=-30, top=30)
    plt.xlim(left=-30, right=30)


    plt.plot(original_figure["x"], original_figure["y"], 'ro-')
    for i_x, i_y in zip(original_figure["x"], original_figure["y"]):
        plt.text(i_x, i_y, f"{i_x}, {i_y}")

    if new_figure != None:
        plt.plot(new_figure["x"], new_figure["y"], 'bo--')
        for i_x, i_y in zip(new_figure["x"], new_figure["y"]):
            plt.text(i_x, i_y, f"{i_x}, {i_y}")

    plt.show()
    plt.clf()