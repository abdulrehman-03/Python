import turtle
from turtle import Turtle, Screen

jimmy = Turtle()
screen = Screen()


def move_forwards():
    jimmy.forward(10)


def move_back():
    jimmy.back(10)


def turn_right():
    jimmy.right(10)


def turn_left():
    jimmy.left(10)


jimmy.pensize(2)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=turtle.resetscreen)

screen.exitonclick()
