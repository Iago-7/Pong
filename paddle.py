from turtle import Turtle


LEFT_PADDLE_LOCATION_COORDINATES = [(-380, 50), (-380, 30), (-380, 10), (-380, -10), (-380, -30)]
RIGHT_PADDLE_LOCATION_COORDINATES = [(380, 50), (380, 30), (380, 10), (380, -10), (380, -30)]


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.segments = []
        self.paddle_side = side
        if side == "Left":
            self.make_left_paddle()
        elif side == "Right":
            self.make_right_paddle()

    def generic_paddle_maker(self):
        segment = Turtle()
        segment.color("white")
        segment.penup()
        segment.shape("square")
        segment.speed("fastest")
        return segment

    def make_left_paddle(self):
        for location in LEFT_PADDLE_LOCATION_COORDINATES:
            current_segment = self.generic_paddle_maker()
            current_segment.goto(location)
            self.segments.append(current_segment)

    def make_right_paddle(self):
        for location in RIGHT_PADDLE_LOCATION_COORDINATES:
            current_segment = self.generic_paddle_maker()
            current_segment.goto(location)
            self.segments.append(current_segment)

    def move_up(self):
        for segment in self.segments:
            segment.setheading(90)
            segment.forward(20)

    def move_down(self):
        for segment in self.segments:
            segment.setheading(270)
            segment.forward(20)
