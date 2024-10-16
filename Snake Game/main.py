"""main module that handles all game logics"""

# import necessary libraries
import time
from turtle import Screen
from snake_class import Snake
from food_class import Food
from score_class import Score
from wall_class import Wall, BOTTOM_LEFT_CORNER, TOP_RIGHT_CORNER
from const import SCREEN_WIDTH, SCREEN_HEIGHT

# setup the screen
SCREEN = Screen()

SCREEN.setup(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    startx=0,
    starty=0
)

SCREEN.bgcolor("black")
SCREEN.title(titlestring="My Snake Game")
SCREEN.tracer(n=0) # wait for the screen update to render

# create the snake
snake = Snake()
food = Food()
score = Score()
wall = Wall()

# listen the keyboard input to control the snake
keys_functions: dict[Snake] = {
    "Up": snake.head_north,
    "Down": snake.head_south,
    "Left": snake.head_west,
    "Right": snake.head_east
}

for key, func in keys_functions.items():
    SCREEN.onkeypress(
        fun=func,
        key=key
    )

SCREEN.listen()

# game on
GAME_ON = True

while GAME_ON:
    SCREEN.update() # render the updated screen
    time.sleep(.1) # wait a second for before each screen update
    snake.move()

    if snake.snake_head.distance(food) < 20:
        food.refresh()
        score.increase_score()

    if snake.snake_head.xcor() == TOP_RIGHT_CORNER["x"] or \
        snake.snake_head.xcor() == BOTTOM_LEFT_CORNER["x"] or \
            snake.snake_head.ycor() == TOP_RIGHT_CORNER["y"] or \
                snake.snake_head.ycor() == BOTTOM_LEFT_CORNER["y"]:
        GAME_ON = False

# exit the game when clicked on the screen
SCREEN.exitonclick()
