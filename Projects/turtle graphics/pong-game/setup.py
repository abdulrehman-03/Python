from turtle import Turtle


class Partition(Turtle):

    def __init__(self):
        super().__init__()
        self.home()
        self.goto(0, 285)
        self.pendown()
        self.speed("fastest")
        self.setheading(270)
        for i in range(30):
            self.color("white")
            self.forward(10)
            self.color("black")
            self.forward(10)

    def clear_partition(self):
        self.clear()
