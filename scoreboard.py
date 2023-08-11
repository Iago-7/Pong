from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, coordinates):
        super().__init__()
        self.goto(coordinates)
        self.score = 0
        self.penup()
        self.ht()
        self.color("white")
        self.write_text()

    def add_point(self):
        self.score += 1
        self.clear()
        self.write_text()

    def write_text(self):
        self.write(self.score, align="center", font=("Arial", 36, "normal"))

    def game_over(self, winning_side):
        self.goto(0, 0)
        self.write(f"The {winning_side} player has won!", align="center", font=("Arial", 20, "normal"))
