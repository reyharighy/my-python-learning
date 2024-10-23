"""Main module to control all funtionality within the game."""

import time
from turtle import Screen
from player import Player
from const import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    PLAYER_STARTING_POS_Y
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

    if crosser.ycor() >= -(PLAYER_STARTING_POS_Y):
        crosser.goto_starting_position()

SCREEN.exitonclick()
