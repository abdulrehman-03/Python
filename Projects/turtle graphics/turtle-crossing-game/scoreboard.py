from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 0
        self.update_level()

    # Updating level and writing it on top of screen
    def update_level(self):
        self.level += 1
        self.clear()
        self.goto(-290, 260)
        self.write(f"Level: {self.level}", font=FONT)

    # Print game over
    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=FONT)

    # Print game end
    def game_end(self):
        self.home()
        self.write("Good Job! You finished all levels", align="center", font=FONT)

