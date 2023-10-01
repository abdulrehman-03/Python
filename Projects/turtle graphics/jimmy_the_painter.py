from turtle import Turtle, Screen
import random

color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

screen = Screen()
jimmy = Turtle()
screen.colormode(255)
jimmy.speed("fastest")
jimmy.penup()
jimmy.hideturtle()

# Starting co-ordinates
x = -230
y = -275

for i in range(10):
    y = y+50
    jimmy.penup()
    jimmy.setpos((x, y))
    for _ in range(10):
        jimmy.pencolor(random.choice(color_list))
        jimmy.dot(15)
        jimmy.forward(50)

screen.exitonclick()
