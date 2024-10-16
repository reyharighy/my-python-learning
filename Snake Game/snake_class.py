"""Module to control the behaviour of the snake"""

from turtle import Turtle
from const import (
    INITIAL_TOTAL_SNAKE_SEGMENTS,
    SNAKE_BODY_SEGMENT_SIZE,
    NORTH, SOUTH, WEST, EAST
)

class Snake:
    """The snake class"""
    def __init__(self) -> None:
        self.the_snake: list[Turtle] = []
        self.create_snake()
        self.snake_head = self.the_snake[0]
        self.reversed_snake_body = self.the_snake[1:][::-1]
        self.snake_body_length = len(self.reversed_snake_body)

    def create_snake(self) -> None:
        """Create the snake for a total number of segments."""
        for i in range(INITIAL_TOTAL_SNAKE_SEGMENTS):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(
                x=-(i*SNAKE_BODY_SEGMENT_SIZE),
                y=0
            )

            self.the_snake.append(new_segment)

    def move(self) -> None:
        """
        Move the snake for each screen update by getting each body segment to move to.
        Its preceeding segment all the way to the head.
        """
        for i, segment in enumerate(iterable=self.reversed_snake_body):
            if i < self.snake_body_length - 1: # obtain except the first body segment to move
                segment.goto(
                    x=self.reversed_snake_body[i + 1].xcor(),
                    y=self.reversed_snake_body[i + 1].ycor()
                )
            else: # get the first body segment to follow the head
                segment.goto(
                    x=self.snake_head.xcor(),
                    y=self.snake_head.ycor()
                )

        self.snake_head.forward(SNAKE_BODY_SEGMENT_SIZE)

    def head_control(self, heads: tuple[int]) -> None:
        """
        Control the behaviour of snake headings when detecting any keyboard input.
        Snake musn't go back from its current direction.

        Args:
            heads: tuple[int]: pair of headings to validate
                               first value is the head to take
                               second value is the head to validate
        """
        # if current headings is the opposite of the headings to take, refuse it
        angle = heads[0] if self.snake_head.heading() != heads[1] else heads[1]
        self.snake_head.setheading(to_angle=angle)

    def head_north(self) -> None:
        """Control the snake heading to go north in direction."""
        self.head_control(heads=(NORTH, SOUTH))

    def head_south(self) -> None:
        """Control the snake heading to go south in direction."""
        self.head_control(heads=(SOUTH, NORTH))

    def head_west(self) -> None:
        """Control the snake heading to go west in direction"""
        self.head_control(heads=(WEST, EAST))

    def head_east(self) -> None:
        """Control the snake heading to go east in direction"""
        self.head_control(heads=(EAST, WEST))
