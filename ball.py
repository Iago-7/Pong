from turtle import Turtle


INITIAL_MOVE_DISTANCE = 10


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 1
        self.y_move = 1
        self.direction = "right"

    def move(self):
        new_x_coord = self.xcor() + self.x_move
        new_y_coord = self.ycor() + self.y_move
        self.goto(new_x_coord, new_y_coord)

    def y_direction_reversal(self):
        self.y_move *= -1

    def x_direction_reversal(self):
        self.x_move *= -1

    def reset_position(self):
        if self.direction == "right":
            self.direction = "left"
        elif self.direction == "left":
            self.direction = "right"
        self.x_direction_reversal()
        self.goto(0, 0)
