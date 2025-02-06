import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Disable automatic screen updates

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.color("red")

# Define the drawing function
def love(t):
    for n in range(0, 360, 1):
        x = 16 * math.sin(math.radians(n))**3
        y = 13 * math.cos(math.radians(n)) - 5 * math.cos(2 * math.radians(n)) - 2 * math.cos(3 * math.radians(n)) - math.cos(4 * math.radians(n))
        t.goto(x, y)

# Draw the shape
t.penup()
t.goto(0, 0)
t.pendown()
love(t)

# Save the drawing as an image
canvas = screen.getcanvas()
canvas.postscript(file="love_drawing.eps")  # Save as EPS

# Optional: Convert EPS to PNG (requires ImageMagick)
import os
os.system("convert love_drawing.eps love_drawing.png")

# Close the turtle graphics window
turtle.bye()
