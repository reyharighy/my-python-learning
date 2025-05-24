"""Module related to ball behaviour with the game environment."""

from turtle import Turtle
from random import randint, choice
from const import RANDOM_DIRECTION_POWER

class Ball(Turtle):
    """The ball class."""
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color('blue')
        self.shape(name="circle")
        self.goto((0, 0)) # set the ball to spawn at the center of the screen
        self.ball_direction = self.set_direction()

    def set_direction(self) -> dict:
        """
        Randomly set the x and y move speed.

        Return:
            dict: get the x and y speed of the ball when moving.
        """
        random_seed = randint(a=10, b=15) * choice(RANDOM_DIRECTION_POWER)

        return {
            "x_speed": random_seed,
            "y_speed": random_seed
        }

    def move(self) -> None:
        """
        Set the ball to move.
        At the initial game, it will move at random direction.
        """
        self.goto(
            x=self.xcor() + self.ball_direction["x_speed"],
            y=self.ycor() + self.ball_direction["y_speed"]
        )

    def hit_wall(self) -> None:
        """Create a behaviour  to bounce when the ball hits the wall."""
        self.ball_direction["y_speed"] *= -1

    def hit_paddle(self) -> None:
        """Create a behaviour to bounce when the ball hits one paddle."""
        self.ball_direction["x_speed"] *= -1

        # each hit with the paddle increases a slight speed
        self.ball_direction["x_speed"] *= 1.1
        self.ball_direction["y_speed"] *= 1.1
