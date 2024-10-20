"""Main module to run all functionality of the game."""

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_NAME,
    BOTTOM_TOP_WALL_Y,
    X_COR
)

# set up the screen
SCREEN = Screen()
SCREEN.bgcolor("black")
SCREEN.title(titlestring=GAME_NAME)
SCREEN.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    startx=0,
    starty=0
)

SCREEN.tracer(n=0) # stop the screen to render the update

# initialize the game objects
l_paddle = Paddle(side="left")
r_paddle = Paddle()
ball = Ball()

control_dict = {
    l_paddle: ["w", "s"],
    r_paddle: ["Up", "Down"]
}

for paddle, key_inputs in control_dict.items():
    for i, key in enumerate(iterable=key_inputs):
        SCREEN.onkeypress(
            fun=paddle.go_up if i % 2 == 0 else paddle.go_down,
            key=key
        )

# start the game
GAME_ON = True
SCREEN.listen()

while GAME_ON:
    time.sleep(.05)
    ball.move()
    SCREEN.update()

    # detect the ball to bounce when hitting either top or bottom wall
    if ball.ycor() >= BOTTOM_TOP_WALL_Y or ball.ycor() <= -(BOTTOM_TOP_WALL_Y):
        ball.hit_wall()

    # test to detect the ball with the paddle
    if (ball.xcor() >= X_COR and ball.distance(r_paddle) < 50)\
          or (ball.xcor() <= -X_COR and ball.distance(l_paddle) < 50):
        ball.hit_paddle()

SCREEN.exitonclick()
