from turtle import Turtle
import time


LEFT_PADDLE_LOCATION_COORDINATES = [(-380, 50), (-380, 30), (-380, 10), (-380, -10), (-380, -30)]


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.make_paddle()
        self.head = self.segments[0]

    def make_paddle(self):
        for location in LEFT_PADDLE_LOCATION_COORDINATES:
            current_segment = Turtle()
            current_segment.color("white")
            current_segment.penup()
            current_segment.shape("square")
            current_segment.goto(location)
            self.segments.append(current_segment)

    def move_up(self):
        self.head = self.segments[0]
        self.setheading(90)
        self.forward(20)


    def move_down(self):
        self.head = self.segments[-1]
