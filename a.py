import tkinter as tk

def get_pixel_color(canvas, x, y):
    # Find the closest canvas item to the specified point (x, y)
    item = canvas.find_closest(x, y)

    if item:
        # Get the fill color of the canvas item
        color = canvas.itemcget(item[0], "fill")
        return color
    else:
        return None

def main():
    # Create a Tkinter window
    window = tk.Tk()
    window.title("Pixel Color Example")

    # Create a canvas widget
    canvas = tk.Canvas(window, width=400, height=400, bg="white")
    
    # Draw a rectangle on the canvas (you can replace this with your own drawings)
    canvas.create_rectangle(100, 100, 300, 300, fill="blue")
    canvas.pack()

    def on_canvas_click(event):
        # Get the mouse click coordinates
        x, y = event.x, event.y

        # Get the color of the pixel at the clicked coordinates
        pixel_color = get_pixel_color(canvas, x, y)

        if pixel_color:
            print(f"Pixel color at ({x}, {y}): {pixel_color}")
        else:
            print(f"No pixel found at ({x}, {y})")

    # Bind the mouse click event to the canvas
    canvas.bind("<Button-1>", on_canvas_click)

    window.mainloop()

if __name__ == '__main__':
    main()