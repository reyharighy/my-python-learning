"""Module to create a wall"""

from turtle import Turtle
from const import X_COR_SPAN, Y_COR_SPAN, MARGIN

BOTTOM_LEFT_CORNER: dict = {"x": -(X_COR_SPAN - MARGIN), "y":-(Y_COR_SPAN - MARGIN)}
BOTTOM_RIGHT_CORNER: dict = {"x": (X_COR_SPAN - MARGIN), "y":-(Y_COR_SPAN - MARGIN)}
TOP_RIGHT_CORNER: dict = {"x": (X_COR_SPAN - MARGIN), "y":(Y_COR_SPAN - MARGIN)}
TOP_LEFT_CORNER: dict = {"x": -(X_COR_SPAN - MARGIN), "y":(Y_COR_SPAN - MARGIN)}
ROUTING_DRAW = [BOTTOM_RIGHT_CORNER, TOP_RIGHT_CORNER, TOP_LEFT_CORNER, BOTTOM_LEFT_CORNER]

class Wall(Turtle):
    """The wall class"""
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        # go to the bottom left first before starting drawing
        self.goto(
            x=BOTTOM_LEFT_CORNER["x"],
            y=BOTTOM_LEFT_CORNER["y"]
        )

        self.pendown()

        for cors in ROUTING_DRAW:
            self.goto(
                x=cors["x"],
                y=cors["y"]
            )
