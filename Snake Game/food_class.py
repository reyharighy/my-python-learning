"""Module to randomly spawn for the snake to get."""

from random import choice
from turtle import Turtle
from const import (
    X_COR_SPAN,
    Y_COR_SPAN,
    STEP
)

FOOD_AREA_WIDTH = list(range(-X_COR_SPAN, X_COR_SPAN, STEP))[2:-1]
FOOD_AREA_HEIGHT = list(range(-Y_COR_SPAN, Y_COR_SPAN, STEP))[2:-1]

class Food(Turtle):
    """The food class"""
    def __init__(self, snake_positions: dict[list]) -> None:
        super().__init__()
        self.shape(name="turtle")
        self.penup()
        self.color("blue")
        self.speed(speed="fastest")
        self.shapesize(1)
        self.refresh(food_positions=self.where(snake_positions=snake_positions))

    def where(self, snake_positions: dict[list]) -> dict[list]:
        """Get the appropriate location of the food outside the snake body"""
        x_cor_span = FOOD_AREA_WIDTH.copy()
        y_cor_span = FOOD_AREA_HEIGHT.copy()

        for pos in snake_positions["x_pos"]:
            print(pos)
            if pos in x_cor_span:
                x_cor_span.remove(pos)

        for pos in snake_positions["y_pos"]:
            if pos in y_cor_span:
                y_cor_span.remove(pos)

        print({"x_span":x_cor_span, "y_span":y_cor_span})
        return {"x_span":x_cor_span, "y_span":y_cor_span}

    def refresh(self, food_positions: dict[list]) -> None:
        """Randomly respawn the food when the snake eats it."""
        self.goto(
            x=choice(food_positions["x_span"]),
            y=choice(food_positions["y_span"])
        )
