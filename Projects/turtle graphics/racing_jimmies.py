from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
is_race_on = True

all_turtles = []
y_axis = -70
for i in range(6):
    jimmies = Turtle(shape="turtle")
    color = colors[i]
    jimmies.color(color)
    jimmies.penup()
    jimmies.goto(x=-230, y=y_axis)
    y_axis += 30
    all_turtles.append(jimmies)

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winners_color = turtle.pencolor()
            if winners_color == user_bet:
                print(f"You've won! The {winners_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winners_color} turtle is the winner!")

        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()
