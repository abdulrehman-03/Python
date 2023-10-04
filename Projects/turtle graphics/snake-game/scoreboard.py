from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.setposition(0, 275)
        self.current_score = 0
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.current_score += 1
        self.write_score()
