from turtle import Turtle


class Background(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.pensize(3)
        self.goto(-290, -290)
        self.pendown()

        for _ in range(4):
            if self.xcor() > 200 and self.ycor() < -200:
                self.forward(560)
            elif self.xcor() < 200 < self.ycor():
                self.forward(560)
            else:
                self.forward(580)
            self.left(90)
