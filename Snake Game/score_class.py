"""Module to write the updated score of the game"""

from turtle import Turtle
from const import Y_COR_SPAN, MARGIN

class Score(Turtle):
    """The score class"""
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(
            x=0,
            y=Y_COR_SPAN - MARGIN
        )

        self.update_score()

    def update_score(self):
        """Show the updated score"""
        self.write(
            arg=f"Score: {self.score}",
            align="center",
            font=("Calibri", 12, "normal")
        )

    def increase_score(self):
        """Increase the score when the snake eats the food"""
        self.score += 1
        self.clear()
        self.update_score()
