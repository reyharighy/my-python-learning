"""Module to set the functionality of the game score."""

from turtle import Turtle
from const import SCREEN_HEIGHT, SCORE_MARGIN

class Scoreboard(Turtle):
    """The scoreboard class."""
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, ((SCREEN_HEIGHT / 2) - SCORE_MARGIN))
        self.write(
            arg="0 - 0",
            align="center",
            font=("Calibri", 12, "bold")
        )

    def increase_score(self, point_to: str):
        """
        When one paddle misses the ball, the opponent gets the score.

        Args:
            point_to (str): which side to grant the score.
        """
        if point_to == "left":
            self.l_score += 1
        else:
            self.r_score += 1

        self.clear()
        self.write(
            arg=f"{self.l_score} - {self.r_score}",
            align="center",
            font=("Calibri", 12, "bold")
        )
