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


jimmy.speed("fastest")
jimmy.pensize(1)

for _ in range(5, 360, 5):
    jimmy.color(random_color())
    jimmy.circle(100)
    jimmy.setheading(_)

screen.exitonclick()
