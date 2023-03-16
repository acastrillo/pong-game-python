from turtle import Screen
from paddle import Paddle
from board_screen_lines import Board_Lines
from ball import Ball
from scoreboard import Scoreboard
import time

# Create the scoreboard
scoreboard = Scoreboard()

# Create the screen
SCREENHEIGHT = 600
SCREENWIDTH = 800
screen = Screen()
screen.setup(
    width=SCREENWIDTH,
    height=SCREENHEIGHT
)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)
board_lines = Board_Lines()

# Create the paddles
paddles = Paddle()

# Create the ball
pong_ball = Ball()

# Allow the paddles to move
screen.listen()
screen.onkey(key="w", fun = (paddles.move_left_up))
screen.onkey(key="s", fun = (paddles.move_left_down))
screen.onkey(key="Up", fun = (paddles.move_right_up))
screen.onkey(key="Down", fun = (paddles.move_right_down))

# Start the game
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(pong_ball.ball_speed)
    pong_ball.move()


    # Passed a paddle
    if pong_ball.xcor() > 390:
        scoreboard.increase_score("left")
        pong_ball.reset()
    
    if pong_ball.xcor() < -390:
        scoreboard.increase_score("right")
        pong_ball.reset()

    #  Hit the ceiling or floor, bounce off
    if pong_ball.ycor() > 285 or pong_ball.ycor() < -285:
        pong_ball.bounce_wall()

    # Hit a paddle
    if pong_ball.distance(paddles.right_paddle) < 30:
        pong_ball.bounce_paddle()
    
    if pong_ball.distance(paddles.left_paddle) < 30:
        pong_ball.bounce_paddle()

    

screen.exitonclick()