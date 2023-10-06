from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_player()

    # Moving player 10 paces
    def move(self):
        self.forward(10)

    # Reset player to its original position. Useful when user completes a level
    def reset_player(self):
        self.goto(0, -280)

