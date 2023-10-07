from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 13, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.hideturtle()
        self.setposition(0, 275)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.current_score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.current_score = 0
        self.write_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def update(self):
        self.current_score += 1
        self.write_score()
