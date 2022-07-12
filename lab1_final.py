# Author: Meher Kalra
# Date: 29 Jan 2022

from cs1lib import *

# defining paddle, window, ball constants
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 80
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
PADDLE_MOTION = 5
BALL_RADIUS = 11
# defining motion keys
LEFT_DOWN = "z"
LEFT_UP = "a"
RIGHT_DOWN = "m"
RIGHT_UP = "k"
QUIT_GAME = "q"
RESET_GAME = " "
# defining left and right paddle coordinates
STARTING_PADDLE_X_LEFT = 0  # starting x coordinate of the left paddle
STARTING_PADDLE_Y_LEFT = 0  # starting y coordinate of the left paddle
left_paddle_y = STARTING_PADDLE_Y_LEFT

STARTING_PADDLE_X_RIGHT = WINDOW_WIDTH - PADDLE_WIDTH  # starting x coordinate of the right paddle
STARTING_PADDLE_Y_RIGHT = WINDOW_HEIGHT - PADDLE_HEIGHT  # starting y coordinate of the right paddle
right_paddle_y = STARTING_PADDLE_Y_RIGHT

# defining ball coordinates
STARTING_BALL_X = WINDOW_WIDTH / 2
STARTING_BALL_Y = WINDOW_HEIGHT / 2
ball_x_coord = STARTING_BALL_X
ball_y_coord = STARTING_BALL_Y
# defining ball velocities
STARTING_BALL_VX = 5
STARTING_BALL_VY = 5
vx = STARTING_BALL_VX
vy = STARTING_BALL_VY

# assigning boolean values to keys
apressed = False
zpressed = False
kpressed = False
mpressed = False
spacebar = False
game_tracker = False

# detect when keys are being pressed and setting boolean value
def my_kpress(value):
    global apressed, zpressed, kpressed, mpressed, spacebar
    if value == LEFT_UP:
        apressed = True
    if value == LEFT_DOWN:
        zpressed = True
    if value == RIGHT_UP:
        kpressed = True
    if value == RIGHT_DOWN:
        mpressed = True
    if value == QUIT_GAME:
        cs1_quit()
    if value == RESET_GAME:
        spacebar = True

# detect when keys are being released and setting boolean value
def my_krelease(value):
    global apressed, zpressed, kpressed, mpressed, spacebar
    if value == LEFT_UP:
        apressed = False
    if value == LEFT_DOWN:
        zpressed = False
    if value == RIGHT_UP:
        kpressed = False
    if value == RIGHT_DOWN:
        mpressed = False
    if value == RESET_GAME:
        spacebar = False

# Purpose: defining function to draw the left and right paddles
def draw_paddles():
    global STARTING_PADDLE_X_LEFT, left_paddle_y, STARTING_PADDLE_X_RIGHT, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT
    disable_stroke()
    set_fill_color(0.2, 0.4, 0.5)
    draw_rectangle(STARTING_PADDLE_X_LEFT, left_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
    set_fill_color(0.3, 0.3, 0.7)
    draw_rectangle(STARTING_PADDLE_X_RIGHT, right_paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)

# Purpose: defining function to set background color
def set_bg_color():
    set_clear_color(0.7, 1, 0.9)
    clear()

# Purpose: defining function to reset the game when the game ends
def reset_game():
    global ball_x_coord, ball_y_coord, STARTING_BALL_X, STARTING_BALL_Y, vx, vy, STARTING_BALL_VX, STARTING_BALL_VY, spacebar, game_tracker, right_paddle_y, left_paddle_y
    if spacebar == True:
        ball_x_coord = STARTING_BALL_X
        ball_y_coord = STARTING_BALL_Y
        vx = STARTING_BALL_VX
        vy = STARTING_BALL_VY
        right_paddle_y = STARTING_PADDLE_Y_RIGHT
        left_paddle_y = STARTING_PADDLE_Y_LEFT
        game_tracker = True

# Purpose: defining function to draw the ping pong ball
def draw_pong_ball():
    global BALL_RADIUS, STARTING_BALL_X, STARTING_BALL_Y, ball_x_coord, ball_y_coord
    set_fill_color(0.2, 0.2, 0.2)
    draw_circle(ball_x_coord, ball_y_coord, BALL_RADIUS)

# Purpose: function to define the motion of the ball when it hits the paddles or the wall
def ball_motion():
    global ball_x_coord, ball_y_coord, vx, vy, WINDOW_HEIGHT, WINDOW_WIDTH, BALL_RADIUS, game_tracker, right_paddle_y, left_paddle_y, STARTING_PADDLE_Y_RIGHT, STARTING_PADDLE_Y_LEFT
    ball_x_coord = ball_x_coord + vx
    ball_y_coord = ball_y_coord + vy
    if ball_y_coord <= BALL_RADIUS or ball_y_coord >= WINDOW_HEIGHT - BALL_RADIUS:
        vy = -vy
    if ball_x_coord <= BALL_RADIUS or ball_x_coord >= WINDOW_WIDTH - BALL_RADIUS:
        vx = 0
        vy = 0
        game_tracker = False
    if ball_x_coord <= PADDLE_WIDTH + BALL_RADIUS and ball_y_coord >= left_paddle_y and ball_y_coord <= left_paddle_y + PADDLE_HEIGHT:
        vx = -vx
        ball_x_coord = ball_x_coord + BALL_RADIUS*1.5
    if ball_x_coord >= WINDOW_WIDTH - PADDLE_WIDTH - BALL_RADIUS and ball_y_coord >= right_paddle_y and ball_y_coord <= right_paddle_y + PADDLE_HEIGHT:
        vx = -vx
        ball_x_coord = ball_x_coord - BALL_RADIUS*1.5

#function to define the paddle movements on the window
def paddle_movement():
    global PADDLE_HEIGHT, PADDLE_WIDTH, STARTING_PADDLE_X_LEFT, left_paddle_y, STARTING_PADDLE_X_RIGHT, right_paddle_y, game_tracker, apressed, zpressed, mpressed, kpressed
    if game_tracker == False:
        apressed = False
        zpressed = False
        mpressed = False
        kpressed = False
    if apressed and left_paddle_y > 0:
        left_paddle_y = left_paddle_y - PADDLE_MOTION
    if zpressed and left_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        left_paddle_y = left_paddle_y + PADDLE_MOTION
    if kpressed and right_paddle_y > 0:
        right_paddle_y = right_paddle_y - PADDLE_MOTION
    if mpressed and right_paddle_y < WINDOW_HEIGHT - PADDLE_HEIGHT:
        right_paddle_y = right_paddle_y + PADDLE_MOTION


# defining the main draw function to define the movement of the paddles and adding the above functions
def main_draw():
    paddle_movement() # paddle movements
    set_bg_color()  # setting background color
    draw_paddles()  # drawing paddles
    draw_pong_ball()  # drawing ball
    # move ball if game is in progress
    if game_tracker == True:
        ball_motion()
    reset_game()

start_graphics(main_draw, key_press=my_kpress, key_release=my_krelease)
