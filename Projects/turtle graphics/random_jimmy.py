import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
jimmy = Turtle()
screen = Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


jimmy.pensize(7)
jimmy.speed(10)

directions = [0, 90, 180, 270]

for _ in range(250):
    jimmy.forward(20)
    jimmy.color(random_color())
    jimmy.setheading(random.choice(directions))

screen.exitonclick()
