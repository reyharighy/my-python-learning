"""Store all constant values required by other modules"""

NORTH, SOUTH, WEST, EAST = 90, 270, 180, 0
INITIAL_TOTAL_SNAKE_SEGMENTS = 5
SEGMENT_SIZE = 20
MARGIN = 20
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
X_COR_SPAN = int(SCREEN_WIDTH/2)
Y_COR_SPAN = int(SCREEN_HEIGHT/2)

STARTING_POSITION = list(
    zip(
        list(
            range(0, -(SEGMENT_SIZE*INITIAL_TOTAL_SNAKE_SEGMENTS), -SEGMENT_SIZE)
        ),
        [0]*5
    )
)
