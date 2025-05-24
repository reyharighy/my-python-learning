"""Main module to control all funtionality within the game."""

import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from cars import Cars
from const import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    PLAYER_STARTING_POS_Y,
    CAR_STARTING_POS_X,
    CAR_LEAVING_OFFSET
)

SCREEN = Screen()
SCREEN.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    startx=None,
    starty=-50
)

SCREEN.tracer(0)

crosser = Player()
score = Scoreboard()
cars = Cars()

# listen to the user controlling inputs
key_inputs = {
    "Up": crosser.traverse,
    "Down": crosser.step_back
}

for key, func in key_inputs.items():
    SCREEN.onkeypress(
        fun=func,
        key=key
    )

SCREEN.listen()

# start the game
GAME_ON = True

while GAME_ON:
    time.sleep(0.1)
    SCREEN.update()
    cars.spawn_a_car()
    cars.move_cars()
    print(len(cars.all_cars))

    if crosser.ycor() >= -(PLAYER_STARTING_POS_Y):
        crosser.goto_starting_position()
        score.increase_level()

    copy_dict = cars.all_cars.copy()

    for car, _ in copy_dict.items():
        if car.xcor() < -(CAR_STARTING_POS_X + CAR_LEAVING_OFFSET):
            del cars.all_cars[car]

SCREEN.exitonclick()
