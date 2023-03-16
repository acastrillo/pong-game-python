from turtle import Turtle

LEFT_START_COORDINATES = (-380, 0)
RIGHT_START_COORDINATES = (380, 0)

PADDLE_WIDTH = 1
PADDLE_LENGTH = 3

UP = 90
DOWN = 270

MOVE_DISTANCE = 20

class Paddle(Turtle):
    
    def __init__(self):
        self.create_left_paddle(LEFT_START_COORDINATES)
        self.create_right_paddle(RIGHT_START_COORDINATES)

    def create_left_paddle(self,coordinate):
        print("Creating left paddle")
        self.left_paddle = Turtle(shape="square")
        self.left_paddle.color("white")
        self.left_paddle.penup()
        self.left_paddle.setheading(UP)
        self.left_paddle.shapesize(PADDLE_WIDTH, PADDLE_LENGTH)
        self.left_paddle.goto(coordinate)

    def create_right_paddle(self,coordinate):
        print("Creating right paddle")
        self.right_paddle = Turtle(shape="square")
        self.right_paddle.color("white")
        self.right_paddle.penup()
        self.right_paddle.setheading(UP)
        self.right_paddle.shapesize(PADDLE_WIDTH, PADDLE_LENGTH)
        self.right_paddle.goto(coordinate)

    def move_left_up(self):
        self.left_paddle.forward(MOVE_DISTANCE)

    def move_right_up(self):
        self.right_paddle.forward(MOVE_DISTANCE)

    def move_left_down(self):
        self.left_paddle.backward(MOVE_DISTANCE)
        

    def move_right_down(self):
        self.right_paddle.backward(MOVE_DISTANCE)