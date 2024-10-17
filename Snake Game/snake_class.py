"""Module to control the behaviour of the snake."""

from turtle import Turtle
from const import (
    STEP, SEGMENT_SIZE, HEAD_SIZE,
    NORTH, SOUTH, WEST, EAST,
    STARTING_POSITION
)

class Snake:
    """The snake class"""
    def __init__(self) -> None:
        self.the_snake: list[Turtle] = []
        self.create_snake()
        self.snake_head = self.the_snake[0]

    def create_snake(self) -> None:
        """Create the snake for a total number of segments."""
        for position in STARTING_POSITION:
            self.add_segment(position=position)

    def snake_positions(self, current_position = None) -> dict[list]:
        """Get the snake positions at the start of the game"""
        snake_positions: dict[list] = {"x_pos":[], "y_pos":[]}

        if current_position is None:
            current_position = STARTING_POSITION

        for x, y in current_position:
            if x not in snake_positions["x_pos"]:
                snake_positions["x_pos"].append(int(x))

            if y not in snake_positions["y_pos"]:
                snake_positions["y_pos"].append(int(y))

        print(snake_positions)
        return snake_positions

    def add_segment(self, position: tuple[int]) -> None:
        """
        Add new segment either at the start of when the snake eats the food.
        
        Args:
            x: int: the coordinate of x
            y: int: the coordinate of y
        """
        is_start: bool = len(self.the_snake) == 0
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.shape(name="arrow" if is_start else "square")
        new_segment.shapesize(HEAD_SIZE if is_start else SEGMENT_SIZE)
        new_segment.color("red" if is_start else "white")
        new_segment.goto(position)
        self.the_snake.append(new_segment)

    def extend(self) -> None:
        """Extend the snake body when eating the food."""
        self.add_segment(position=self.the_snake[-1].position())

    def move(self) -> None:
        """
        Move the snake for each screen update by getting each body segment to move to.
        Its preceeding segment all the way to the head.
        """
        for segment_idx in range(len(self.the_snake) - 1, 0, -1):
            self.the_snake[segment_idx].goto(
                x=self.the_snake[segment_idx - 1].xcor(),
                y=self.the_snake[segment_idx - 1].ycor()
            )

        self.snake_head.forward(STEP)

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
        """Control the snake heading to go west in direction."""
        self.head_control(heads=(WEST, EAST))

    def head_east(self) -> None:
        """Control the snake heading to go east in direction."""
        self.head_control(heads=(EAST, WEST))
