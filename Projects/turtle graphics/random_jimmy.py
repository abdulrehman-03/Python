from turtle import Turtle, Screen
import random

jimmy = Turtle()
screen = Screen()

colors = ["CornflowerBlue", "DarkRed", "DarkOrchid3", "DarkSlateGray2", "gray40", "gold", "navy", "LightSlateBlue",
          "PaleGreen1"]

jimmy.pensize(7)
jimmy.speed(10)

directions = [0, 90, 180, 270]

for _ in range(250):
    jimmy.forward(20)
    jimmy.color(random.choice(colors))
    jimmy.setheading(random.choice(directions))

screen.exitonclick()
