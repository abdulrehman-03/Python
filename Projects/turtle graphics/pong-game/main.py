from turtle import Screen
from paddles import Paddles
from ball import Ball
from scoreboard import Scoreboard
import setup
import time


screen = Screen()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

ball = Ball()
r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
scoreboard = Scoreboard()
setup = setup.Partition()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score > 9:
        setup.clear_partition()
        scoreboard.game_over("Player 1")
        game_on = False
    elif scoreboard.r_score > 9:
        setup.clear_partition()
        scoreboard.game_over("Player 2")
        game_on = False

screen.exitonclick()
