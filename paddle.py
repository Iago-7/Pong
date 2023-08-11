from turtle import Turtle


PADDLE_Y_AXIS_UPPER_BOUND = 260
PADDLE_Y_AXIS_LOWER_BOUND = -240
PADDLE_MOVE_DISTANCE = 20
FULL_PADDLE_SIZE = 50


class Paddle(Turtle):

    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=(FULL_PADDLE_SIZE/10), stretch_len=1)
        self.speed("fastest")
        self.goto(x_coord, y_coord)

    def move_up(self):
        if self.ycor() < PADDLE_Y_AXIS_UPPER_BOUND:
            new_y_coord = self.ycor() + PADDLE_MOVE_DISTANCE
            self.goto(self.xcor(), new_y_coord)

    def move_down(self):
        if self.ycor() > PADDLE_Y_AXIS_LOWER_BOUND:
            new_y_coord = self.ycor() - PADDLE_MOVE_DISTANCE
            self.goto(self.xcor(), new_y_coord)
