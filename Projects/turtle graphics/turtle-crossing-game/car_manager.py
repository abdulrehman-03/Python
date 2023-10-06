from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.chance = 6

    # Creating car 1 out of 6 chances at first. Increasing chances as level gets up
    def create_car(self):
        random_chance = random.randint(1, self.chance)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    # Moving cars across x-axis
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    # Increasing speed and changing chance of creating car when level increases. self.chance changes the range of
    # random choice, so the car will be created more often. It is to keep it compatible with speed of cars.
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.chance > 1:
            self.chance -= 1
