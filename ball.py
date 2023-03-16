from turtle import Turtle
import random

MOVE_DISTANCE = 20
STARTING_COORDINATE = (0,0)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.ball_speed = 0.1
        self.speed(self.ball_speed)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # self.forward(MOVE_DISTANCE)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.ball_speed = 0.1
        self.goto(0,0)