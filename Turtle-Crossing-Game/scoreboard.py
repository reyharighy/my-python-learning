"""Module to update the current level of the game."""

from turtle import Turtle
from const import (
    SCORE_POS_X,
    SCORE_POS_Y,
    FONT
)

class Scoreboard(Turtle):
    """The scoreboard class."""
    def __init__(self) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(
            x=SCORE_POS_X,
            y=SCORE_POS_Y
        )

        self.update_level()

    def update_level(self) -> None:
        """Update the current level of the game."""
        self.clear()
        self.write(
            arg=f"Level {self.level}",
            align="left",
            font=FONT
        )

    def increase_level(self) -> None:
        """Increase the level when the turtle successfully reach another end."""
        self.level += 1
        self.update_level()
