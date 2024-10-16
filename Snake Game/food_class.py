"""Module to randomly spawn for the snake to get."""

from random import choice
from turtle import Turtle
from const import (
    X_COR_SPAN, 
    Y_COR_SPAN, 
    SEGMENT_SIZE
)

FOOD_AREA_WIDTH = list(range(-X_COR_SPAN, X_COR_SPAN, SEGMENT_SIZE))[2:-1]
FOOD_AREA_HEIGHT = list(range(-Y_COR_SPAN, Y_COR_SPAN, SEGMENT_SIZE))[2:-1]

class Food(Turtle):
    """The food class"""
    def __init__(self) -> None:
        super().__init__()
        self.shape(name="circle")
        self.penup()
        self.color("blue")
        self.speed(speed="fastest")
        self.refresh()
        self.shapesize(
            stretch_len=1,
            stretch_wid=1
        )

    def refresh(self) -> None:
        """Randomly respawn the food when the snake eats it."""
        self.goto(
            x=choice(FOOD_AREA_WIDTH),
            y=choice(FOOD_AREA_HEIGHT)
        )
