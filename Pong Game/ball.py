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
        self.ball_speed = self.set_direction()

    def set_direction(self) -> dict:
        """
        Randomly set the x and y move speed

        Return:
            dict: get the x and y speed of the ball when moving.
        """
        return {
            "x_speed": randint(a=5, b=10) * choice(RANDOM_DIRECTION_POWER), 
            "y_speed": randint(a=5, b=10) * choice(RANDOM_DIRECTION_POWER)
        }

    def move(self):
        """
        Set the ball to move.
        At the initial game, it will move at random direction.
        """
        self.goto(
            x=self.xcor() + self.ball_speed["x_speed"],
            y=self.ycor() + self.ball_speed["y_speed"]
        )

    def hit_wall(self):
        """Create a behaviour when the ball hits the wall to bounce"""
        self.ball_speed["y_speed"] *= -1
