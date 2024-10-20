"""Module related to paddles object in the game."""

from turtle import Turtle
from const import (
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_MOVE_SPEED,
    X_COR, Y_COR
)

class Paddle(Turtle):
    """
    The paddle class.

    Args:
        side (str): The position of the paddle. Either left or right.
                    Unless specified, the side will be on the right of the screen.
                    The valid input is only "left". 
    """
    def __init__(self, side: str = None) -> None:
        super().__init__()
        self.penup()
        self.setheading(to_angle=180)
        self.color("white")

        # the setup ratio is opposite with the screen setting
        self.shapesize(
            stretch_wid=PADDLE_HEIGHT,
            stretch_len=PADDLE_WIDTH
        )

        self.x_cor = X_COR

        if side == "left":
            self.x_cor *= -1
            self.setheading(to_angle=0)

        self.goto(
            x=self.x_cor,
            y=0
        )

    def go_up(self):
        """Make the paddle to move up based-on the user key input."""
        if self.ycor() < Y_COR:
            self.goto(
                x=self.xcor(),
                y=self.ycor() + PADDLE_MOVE_SPEED
            )

    def go_down(self):
        """Make the paddle to move down based-on the user key input."""
        if self.ycor() > -Y_COR:
            self.goto(
                x=self.xcor(),
                y=self.ycor() - PADDLE_MOVE_SPEED
            )
