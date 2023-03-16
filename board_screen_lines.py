from turtle import Turtle

SCREENHEIGHT = 600

NUM_OF_LINES = SCREENHEIGHT / 5

LINE_WIDTH = 0.5
LINE_HEIGHT = 1.7

UP = 90

LINE_COORDS = [(0,0), 
               (0,50), (0,-50), 
               (0,100), (0,-100), 
               (0,150), (0,-150),
               (0,200), (0,-200),
               (0,250), (0,-250),
               (0,300), (0,-300)]

class Board_Lines():
    def __init__(self):
        for coordinate in LINE_COORDS:
            self.create_board_line(coordinate)

    def create_board_line(self, coordinate):
        self.line = Turtle(shape="square")
        self.line.color("white")
        self.line.penup()
        self.line.goto(coordinate)
        self.line.setheading(UP)
        self.line.shapesize(LINE_WIDTH, LINE_HEIGHT)