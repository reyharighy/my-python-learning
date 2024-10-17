"""Store all constant values required by other modules"""

NORTH, SOUTH, WEST, EAST = 90, 270, 180, 0 # the angle using complete system
INITIAL_TOTAL_SNAKE_SEGMENTS = 5
HEAD_SIZE = 1.25
SEGMENT_SIZE = .75
STEP = 20
MARGIN = 20 # from the screen sides
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
X_COR_SPAN = int(SCREEN_WIDTH/2)
Y_COR_SPAN = int(SCREEN_HEIGHT/2)

# create the initial positions of segments when the game starts
STARTING_POSITION = list(zip(
    list(range(0, -(STEP*INITIAL_TOTAL_SNAKE_SEGMENTS), -STEP)), # xcors
    [0]*INITIAL_TOTAL_SNAKE_SEGMENTS                             # ycors
))
