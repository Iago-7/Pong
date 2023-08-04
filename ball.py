from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def initial_move(self):
        random_heading = randint(136, 224)
        self.setheading(random_heading)
        self.forward(20)

    def move(self):
        self.forward(20)
