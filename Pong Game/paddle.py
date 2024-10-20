"""Module related to paddles object in the game."""

from turtle import Turtle
from const import (
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    PADDLE_MOVE_SPEED,
    Y_COR, X_PADDLE
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
        self.shape(name="square")
        self.setheading(to_angle=180)
        self.color("white")

        # the setup ratio is opposite with the screen setting
        self.shapesize(
            stretch_wid=PADDLE_HEIGHT,
            stretch_len=PADDLE_WIDTH
        )

        self.x_paddle = X_PADDLE

        if side == "left":
            self.x_paddle *= -1
            self.setheading(to_angle=0)

        self.goto(
            x=self.x_paddle,
            y=0
        )

    def go_up(self) -> None:
        """Make the paddle to move up based-on the user key input."""
        if self.ycor() < Y_COR:
            self.goto(
                x=self.xcor(),
                y=self.ycor() + PADDLE_MOVE_SPEED
            )

    def go_down(self) -> None:
        """Make the paddle to move down based-on the user key input."""
        if self.ycor() > -Y_COR:
            self.goto(
                x=self.xcor(),
                y=self.ycor() - PADDLE_MOVE_SPEED
            )
