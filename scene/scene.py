# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    # Call the finish_drawing function
    # in the draw2d.py library.
   
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_sky(canvas, scene_width, scene_height):
    """Draw the sky and all the objects in the sky."""
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="sky blue")

    draw_cloud(canvas, 20, 415)
    draw_cloud(canvas, 200, 350)
    draw_cloud(canvas, 350, 200)
    draw_cloud(canvas, 600, 275)
    draw_cloud(canvas, 650, 450)


def draw_ground(canvas, scene_width, scene_height):
    """Draw the ground and all the objects on the ground."""
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="tan4")


def draw_cloud(canvas, cloud_x, cloud_y):
    """Draw a cloud with random hights of random ovals in the specified parameters."""
    my_int = 0
    number = random.randint(1, 6)
    if number == 1:
        my_int = 15
    if number == 2:
        my_int = -15
    if number == 3:
        my_int = 25
    if number == 4:
        my_int = -25
    if number == 35:
        my_int = 5
    if number == 6:
        my_int = -35

    draw_rand_oval(canvas, cloud_x, cloud_y)
    draw_rand_oval(canvas, cloud_x + my_int, cloud_y + my_int)
    draw_rand_oval(canvas, cloud_x + my_int, cloud_y)
    draw_rand_oval(canvas, cloud_x, cloud_y + my_int)

def draw_rand_oval(canvas, rand_x, rand_y):
    """Draw random ovals within the specified parameters"""
    diameter = 25
    space = 25
    interval = diameter + space

    for i in range(5):
        number = random.randint(1, 4)
        if number > 1:
            draw_oval(canvas, (rand_x * .25), rand_y,
                    rand_x + diameter, rand_y + diameter, outline = "white", fill="white")
            draw_oval(canvas, rand_x*.75, rand_y, rand_x + diameter * 1.5, rand_y + diameter * 1.5 , outline = "white", fill="white")
        rand_x += interval


# Call the main function so that
# this program will start executing.
main()