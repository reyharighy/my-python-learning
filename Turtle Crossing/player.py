"""Module to control the functionality of the player."""

from turtle import Turtle
from const import (
    PLAYER_STARTING_POS,
    PLAYER_STARTING_POS_Y,
    TRAVERSE,
    STEP_BACK
)

class Player(Turtle):
    """The player class."""
    def __init__(self) -> None:
        super().__init__()
        self.shape(name="turtle")
        self.setheading(to_angle=90)
        self.penup()
        self.goto_starting_position()

    def goto_starting_position(self) -> None:
        """
        Get the player to go to the starting position.
        This condition happens at the game initialization
        and when the player reaches the other side.
        """
        self.goto(PLAYER_STARTING_POS)

    def basic_move_func(self, action: str = None) -> None:
        """
        Combine similar functionalities of moving in one method distinguished by the input.

        Args:
            action (str): Action to do for the player.
        """
        if action is None:
            action = "traverse"

        self.goto(
            x=self.xcor(),
            y=self.ycor() + (TRAVERSE if action == "traverse" else STEP_BACK)
        )

    def traverse(self) -> None:
        """Get the player to move across the road."""
        self.basic_move_func()

    def step_back(self) -> None:
        """Get the player to step back a bit."""
        if self.ycor() > PLAYER_STARTING_POS_Y:
            self.basic_move_func(action="step back")
