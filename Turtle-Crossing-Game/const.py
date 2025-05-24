"""Store all constants needed for other module to access."""

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
MARGIN = 20

PLAYER_STARTING_POS_Y = -((SCREEN_HEIGHT / 2) - MARGIN)
PLAYER_STARTING_POS = (0, PLAYER_STARTING_POS_Y)
TRAVERSE = 10
STEP_BACK = -5

SCORE_POS_X = -((SCREEN_WIDTH / 2) - MARGIN)
SCORE_POS_Y = (SCREEN_HEIGHT / 2) - (MARGIN * 2)
FONT = ("Calibri", 14, "bold")

CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_STARTING_POS_X = SCREEN_WIDTH / 2
CAR_STARTING_POS_Y = list(range(-int(SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT / 2), MARGIN))[3:-2]
CAR_SPEED = list(range(10, 21))

# the ratio to the power of 20
CAR_X_RATIO = 1.5
CAR_Y_RATIO = .8

CAR_LEAVING_OFFSET = 50
