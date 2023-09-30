from turtle import Turtle, Screen
import random

jimmy = Turtle()
colors = ["CornflowerBlue", "DarkRed", "DarkOrchid3", "DarkSlateGray2", "gray40", "gold", "navy", "LightSlateBlue",
          "PaleGreen1"]

jimmy.pensize(7)

for _ in range(3, 10):
    angle = 360 / _
    for t in range(_):
        jimmy.forward(100)
        jimmy.right(angle)
    jimmy.color(random.choice(colors))

screen = Screen()
screen.exitonclick()
