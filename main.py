import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")

def love(t):
    for n in range(0, 360, 1):
        x = 16 * math.sin(math.radians(n))**3
        y = 13 * math.cos(math.radians(n)) - 5 * math.cos(2 * math.radians(n)) - 2 * math.cos(3 * math.radians(n)) - math.cos(4 * math.radians(n))
        
        t.goto(x, y)


t.penup()
t.goto(0, 0)
t.pendown()
love(t)

t.hideturtle()
turtle.done()
