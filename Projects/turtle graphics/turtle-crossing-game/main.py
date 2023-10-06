import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting up turtle screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Creating instances
score = Scoreboard()
player = Player()
car_manager = CarManager()

# Detecting input for when to move
screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Creating and moving cars (more like bricks though)
    car_manager.create_car()
    car_manager.move_cars()

    # Reset players position and increase level and speed if player has made it to the end of wall
    if player.ycor() > 280:
        score.update_level()
        car_manager.level_up()
        player.reset_player()

    # End game if player finishes 10 levels
    if score.level > 10:
        score.game_end()
        break

    # Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False


screen.exitonclick()
