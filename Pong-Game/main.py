"""Main module to run all functionality of the game."""

import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from const import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_NAME,
    X_COR, Y_COR
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
ball = Ball()
l_paddle = Paddle(side="left")
r_paddle = Paddle()
scoreboard = Scoreboard()

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
    if ball.ycor() >= Y_COR or ball.ycor() <= -(Y_COR):
        ball.hit_wall()

    # detect the ball to bounce when hitting the paddle
    if (ball.xcor() >= X_COR and ball.distance(r_paddle) < 50)\
          or (ball.xcor() <= -X_COR and ball.distance(l_paddle) < 50):
        ball.hit_paddle()

    # detect when the paddle misses the ball
    if ball.xcor() > (SCREEN_WIDTH / 2) or ball.xcor() < -(SCREEN_WIDTH / 2):
        if ball.xcor() > 0:
            scoreboard.increase_score(point_to="left")
        else:
            scoreboard.increase_score(point_to="right")

        ball.ball_direction = ball.set_direction()
        ball.goto(0, 0)

SCREEN.exitonclick()
